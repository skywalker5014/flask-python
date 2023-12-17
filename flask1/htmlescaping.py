from markupsafe import escape
from flask import Flask

app = Flask(__name__)


@app.route("/")

def hello(name):
    return f"hello there, {escape(name)}"

