#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
My first Flask app
"""
# Importera relevanta moduler
from flask import Flask, render_template
from person import Person

# import person.py

app = Flask(__name__, static_url_path="/static")

name = "Olov Wimark"
course = "Nortbound"

@app.route("/")
def main():
    """ Main route """
    # return "Välkommen!"
    return render_template("index.html", name=pn.firstN, school=pn.school)

@app.route("/about")
def about():
    """ About route """
    # return render_template("about.html", name=pn.firstName, course=my_course)
    return render_template("about.html", name=name, course=course)

@app.route("/redovisa")
def redovisa():
    """Redovisning - report"""
    return render_template("redovisning.html")

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found - 404
    """

    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """

    #pylint: disable=unused-argument
    import traceback
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    pn = Person('olov')

    app.run()
