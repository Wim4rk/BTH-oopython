#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Contains the handler/manager class for the questions.
"""

import pdb
import json

from questions import Question, CheckboxQuestion, RadiobuttonQuestion

class QuestionManager():
    """
    Manages all questions
    """

    def __init__(self):
        self._points = 0
        self._quest_count = 0
        self._questions = ''
        self._question = []


    def get_score(self):
        """
        Return score
        """
        pass


    def get_max_score(self):
        """
        Return max score
        """
        pass


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
        return self._question[self._quest_count]


    def get_quest_count(self):
        """
        Return the number of questions in json file
        Number should be stored in self.quest_count
        """
        pass


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


    def correct_answer(self, form):
        """
        Return correct answer
        """
        question = self.get_next()

        if Question.type == "text" or RadiobuttonQuestion.type == "radiobutton":
            print(question)
            self._points += question.check_answer (form.getList("answer"))
        elif Checkboxquestion.type == "checkbox":
            self._points += question.check_answer (form.getList("answer"))
        self._quest_count += 1
