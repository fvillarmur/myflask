"""hello"""
from flask import Flask, render_template, request

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
