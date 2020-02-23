#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Contains the handler/manager class for the questions.
"""

import json
# import pdb
# import pprint

from questions import Question, CheckboxQuestion, RadiobuttonQuestion

# pylint: disable=unused-variable

class QuestionManager():
    """
    Manages all questions
    """

    def __init__(self):
        self._points = 0
        self._quest_count = 0
        self._last_question = 0
        self._questions = self._list_questions()


    def _list_questions(self):
        """Load every question into this class"""

        # This is done every time, it shouldnt be.
        # It could be, so long as the order is the same
        # every time...

        # pdb.set_trace()
        local_list = []
        jdata = json.load(open("questions.json", encoding="utf-8"))

        # for quest in jdata.keys():
        for i, quest in enumerate(jdata):
        # for i in jdata.
            # pp = pprint.PrettyPrinter(indent=4)
            # pp.pprint(jdata)
            # print("jdata - nyckel " + quest)

            txt = jdata[quest]["question"]
            switch = jdata[quest]["type"]
            answ = jdata[quest]["answer"]
            number = quest

            # print(number)

            if switch == "radiobutton":
                alts = jdata[quest]["alt"]
                new_obj = RadiobuttonQuestion(number, txt, answ, alts)
            elif switch == "checkbox":
                alts = jdata[quest]["alt"]
                new_obj = CheckboxQuestion(number, txt, answ, alts)
            else:
                new_obj = Question(number, txt, answ)

            # print(quest)
            # print(type(quest))
            # print(type(new_obj))

            # pdb.set_trace()

            local_list.append(new_obj)

        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(local_list)

        local_list.sort(key=lambda quest_obj: quest_obj.get_number())

        # print(local_list)

        self._last_question = len(local_list)
        # pdb.set_trace()
        # print("Antal frågor: {}".format(self._last_question))
        return local_list

    def get_score(self):
        """
        Return score
        """
        # pdb.set_trace()
        return self._points


    def get_max_score(self):
        """
        Return max score
        """
        score = 0
        for question in self._questions:
            score += question.get_max_points()

        return score

    def has_next(self):
        """
        Are there more questions?
        Return boolean
        """
        # (print("_quest_count is {} of {} questions"
        #        .format(self._quest_count, self._last_question)))
        return self._quest_count < self._last_question


    def get_next(self):
        """
        Return next question
        """
        return self._questions[self._quest_count]


    def get_quest_count(self):
        """
        Return the number of questions in list
        """
        return self._last_question


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
        Reset score and quest count to 0
        """
        # pdb.set_trace()
        self._quest_count = 0
        self._points = 0
        # pdb.set_trace()


    def correct_answer(self, form):
        """
        Return correct answer
        """
        question = self.get_next()

        # print("Fråga nummer: ", question)
        # pdb.set_trace()
        if Question.type == "text" or RadiobuttonQuestion.type == "radiobutton":
            # print(question)
            self._points += question.check_answer(form.getlist("answer"))
        elif CheckboxQuestion.type == "checkbox":
            self._points += question.check_answer(form.getlist("answer"))
        self._quest_count += 1
