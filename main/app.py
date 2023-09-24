"""hello"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    """document home"""
    return 'hellou'

@app.route("/about")
def about():
    """about doc"""
    return 'about'