from flask import render_template
from . import main

@main.route("/")
def index():
    return render_template("index.html")
    # return "<h1>test</h1>"
