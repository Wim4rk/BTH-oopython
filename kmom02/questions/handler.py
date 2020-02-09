#!/usr/bin/env python3
"""
Contains the handler/manager class for the questions.
"""

import json

class QuestionManager():
    """
    Manages all questions
    """

    def __init__(self):
        self._points = 0
        self._quest_count = 0
        self.questions = 

    def has_next(self, question):
        """
        Is there a next question?
        ret boolean
        """

        # Max number of questions?
        maxQ = get_max()
        if question >= maxQ:
            # There is no next question
            return False

        return True

    def get_next(self, question):
        """
        If there is a next question, it is returned
        """
        if has_next(question):
            # Return the question number

        return False

    def get_max(self):
        """
        Return the number of questions in json file
        """

    def read_session(self, session):
        """
        Read current score and current quest number from session
        """
        self._points = session.get("points", 0)
        self._quest_count = session.get("quest_count", 0)

    def write_session(self, session):
        """
        Write current score and quest number to session
        """
        session["points"] = self._points
        session["quest_count"] = self._quest_count

    def reset(self):
        """
        Reset score and quest number to 0
        """
        self._quest_count = 0
        self._points = 0
        return redirect(url_for('main'))
