#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Main app for employee."""
import traceback
import os
import re
# import pdb
from flask import Flask, render_template, request, session, redirect, url_for
from handler import Handler
# pylint: disable=unused-argument
# pylint: disable=C0103

app = Flask(__name__)
handler = Handler()

app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

@app.route("/")
def main():
    """Output main route."""
    handler.read_session(session)
    return render_template("index.html", people=handler.get_people())


@app.route("/company", methods=["POST", "GET"])
def company():
    """ Company route """

    handler.read_session(session)

    if request.method == "POST":
        # pdb.set_trace()
        handler.add_employee(request.form)
        handler.write_session(session)

    return render_template("company.html", persons=handler.get_people())

@app.route("/reset")
def reset():
    """Route for reset session"""
    _ = [session.pop(key) for key in list(session.keys())]

    # Destroy class instance
    handler.people = []
    handler.add_predefined_employees()

    return redirect(url_for("main"))


@app.errorhandler(404)
def page_not_found(e):
    """Output page not found 404."""
    # pylint: disable=unused-argument
    return "Flask 404 here, but not the page you're looking for"


@app.errorhandler(500)
def internal_server_error(e):
    """Handle internal server error 500."""
    return "<p>Flask 500<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run(debug=True)
