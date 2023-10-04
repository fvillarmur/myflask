 # pylint: disable=E1101
"""hello"""
import base64
from io import BytesIO
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import mpld3
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    """document home"""
    return render_template('hello.html')

@app.route("/about")
def about():
    """about doc"""
    return 'about'

@app.route('/path/<name>')
def get_path(name=None):
    """get path param"""
    return render_template('path.html', name=name)

@app.route('/params')
def get_query_params():
    """/params?param=oli query params"""
    variable=request.args['param']
    return render_template('queryParams.html', param=variable)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """login post"""
    if request.method == 'POST':
        return render_template('loged.html', username=request.form['username'])
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/graph')
def graph():
    """Generate the figure **without using pyplot"""
    fig = Figure()
    a_x = fig.subplots()
    a_x.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

@app.route('/graph/interactive')
def graph_interactive():
    """Generate the figure **without using pyplot"""
    fig, a_x = plt.subplots()
    # dummy data
    _x = np.linspace(0, 2 * np.pi, 400)
    _y = 1000 * np.sin(_x ** 2)
    a_x.plot(_x, _y)
    a_x.set_title("Plot with grid")
    # draw gridlines
    a_x.grid(True)
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")

    #tooltip = mpld3.plugins.LineLabelTooltip(_x[0])
    #mpld3.plugins.connect(fig, tooltip)

    #Embed the result in the html output.
    html_str = mpld3.fig_to_html(fig)
    print(html_str)
    return f"{html_str}"
