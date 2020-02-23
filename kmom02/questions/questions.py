#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Contains all classes for the different types of questions
"""

class Question():
    """
    Handles questions
    """

    type = "text"

    def __init__(self, number, text, answer):
        """
        Constructor
        """
        self._text = text
        self._answer = answer
        self._number = number


    @classmethod
    def get_type(cls):
        """Return question type"""
        # print("Class method called")
        return cls.type


    def get_text(self):
        """
        Returns the question itself,
        to be used on the html-form
        ret: string
        """
        return self._text

    @classmethod
    def get_max_points(cls):
        """
        Return max points for this->question
        Used for calculating max score in handler
        """
        #  print("{}: {}".format(self._text, 1))
        return 1


    def get_number(self):
        """Return number of current cuestion"""
        return self._number


    def check_answer(self, respons):
        """
        Checks if answer is correct
        """

        # pdb.set_trace()

        return self._answer.lower() == respons[0].lower()


class RadiobuttonQuestion(Question):
    """
    Handles a radiobutton question
    """

    type = "radiobutton"

    def __init__(self, number, text, answer, alternatives):
        """Constructor."""
        self._alternatives = alternatives

        super().__init__(number, text, answer)


    def get_alternatives(self):
        """Return a list."""
        return self._alternatives


class CheckboxQuestion(Question):
    """
    Handles a checkbox question
    Checkboxes can have many answers
    So 'answers' is a list
    """

    type = "checkbox"

    def __init__(self, number, text, answer, alternatives):
        """Setup this question"""
        self._alternatives = alternatives

        super().__init__(number, text, answer)

    def get_alternatives(self):
        """Return a list."""
        return self._alternatives

    def get_max_points(self):
        """
        Return max points for this->question
        Used for calculating max score in handler
        """
        # print("{}: {}".format(self._text, len(self._answer)))
        return len(self._answer)


    def check_answer(self, respons):
        """Compare lists, return integer"""

        # respons = respons.getlist("answer")
        points = 0
        for answer in respons:
            if answer.lower() in self._answer:
                points += 1
            else:
                points -= 1

        return points
