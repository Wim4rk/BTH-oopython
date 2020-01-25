#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
from flask import Flask, render_template

app = Flask(__name__)

my_name = "Olov Wimark"
my_course = "OOPython"

@app.route("/")
def main():
    """ Main route """
    # return "Välkommen!"
    return render_template("index.html")

@app.route("/about")
def about():
    """ About route """
    return render_template("about.html", name=my_name, course=my_course)

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found - 404
    """

    #pylint: disable=unused-argument
    return "Flask 404 here, bot not the page you requested."

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """

    #pylint: disable=unused-argument
    import traceback
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    app.run()
