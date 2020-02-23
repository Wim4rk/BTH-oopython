#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Minimal Flask application, including useful error handlers.
"""

import os
import re
# import pdb
from flask import Flask, render_template, request, redirect, url_for, session
from handler import QuestionManager

# pylint: disable=unused-variable

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

QM = QuestionManager()
# pdb.set_trace()

@app.route("/")
def main():
    """
    Home route
    Shows welcome page and link to start questions
    """
    return render_template("index.html")

# pylint: disable=unused-variable

@app.route("/question", methods=["POST", "GET"])
def question():
    """
    Question route
    Used to display current question.
    If POST request, a user has answered a question.
    If there are no more questions redirect to score screen route.
    """
    QM.read_session(session)

    # happens when a user answers a question
    if request.method == "POST":
        QM.correct_answer(request.form)
        QM.write_session(session)

    if QM.has_next():
        # pdb.set_trace()
        return render_template("question.html", question=QM.get_next())

    return redirect(url_for('score_screen'))

# pylint: disable=unused-argument
@app.route("/score_screen", methods=["GET"])
def score_screen():
    """
    Score screen
    Shows how many correct answers the user got and max score.
    """
    QM.read_session(session)

    return render_template("score_screen.html",
                           score=QM.get_score(),
                           max_score=QM.get_max_score())


@app.route("/reset")
def reset():
    """
    Reset questcount and session so the user can start over.
    """
    _ = [session.pop(key) for key in list(session.keys())]

    QM.reset()

    return redirect(url_for("main"))


@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    import traceback
    return "<p>Flask 500<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run(debug=True)
