#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Contains all classes for the different types of questions
"""

Class Question():
"""
Handles questions
"""

    type = "text"

    def __init__(self, text, answer, question):
        """
        Constructor
        """
        self.type = ""
        self._answer = ""
        self._text = ""
        self._questions = list_questions()


    @classmethod
    def get_type(cls):


    def _get_question(self, question):
        """
        Opens the question from where it's stored

        Question is
        """

        # If question is radiobutton, create radiobutton object

        # If question is checkbox, create checkbox question

        # Store question in self.question

    def list_questions(self):
        """
        Load every question into this class
        """
        # Open Json
        return json.load(open("questions.json", encoding="utf-8"))


    @classmethod
    def get_type():
        """
        Return type for question. Text, radiobuttons, checkbox?
        Returns string
        + checkbox
        + radiobutton
        + text
        """


    def check_answer(self, respons):
        """
        Checks if answer is correct
        """

        respons = respons.get("answer")
        return self._answer.lower() == respons.lower()


    def get_text(self):
        """
        Returns the question itself,
        to be used on the html-form
        ret: string
        """

        # In order to return text, get current question


class RadibuttonQuestion(Question):
    """
    Handles a radiobutton question
    """

    type = "radiobutton"

    def __init__(text, answer, alternatives):
        """Constructor."""


        pass

    def get_alternatives(self):
        """Return a list."""
        pass


class CheckboxQuestion(Question):
    """
    Handles a checkbox question
    Checkboxes can have many answers
    So 'answers' is a list
    """

    type = "checkbox"

    def __init__(text, answers, alternatives):
        """Setup this question"""
        self.alternatives = alternatives

        __super__(text, answers)


    def get_alternatives(self):
        """Return list of alternatives"""


    def check_answer(self, respons):
        """For each alternative, return True or False."""

        respons = respons.geList("answer")
        points = 0
        for v in respons:
            if v in self._answer
                points += 1
        return points

"""
Hur ser frågorna ut? Vad behöver de innehålla.

1. Själva frågan, en sträng
2. Typ av fråga - text, radio, check
3. Svarsalternativ, okänt antal (Lista, dict med siffra som nyckel?).
4. Rätt svar. Format? Siffror, strängar för ensvarsalternativ?
    Kan jag göra allt med strängar?

Hur radar man bäst upp fyra alternativ? Egentligen i en databas, men vaf.
Vi har lärt oss om Json...

{
    "question_no":"1",
    "question":"Vad är det som går och går...?",
    "answer":"klockan",
    "alternative":
    [
        "1":"En långsam katt",
        "2":"En osthyvel",
        "3":"Klockan",
        "4":"Åt fanders"
    ]
}

"""
