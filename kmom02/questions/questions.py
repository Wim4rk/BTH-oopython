"""
Contains all classes for the different types of questions
"""

Class Question():
"""
Handles questions
"""

    def __init__(self, text, answer, question):
        """
        Constructor
        """
        self._answer = ""
        self._text = ""
        self._questions = list_questions()

    def _get_question(self, question):
        """
        Opens the question from where it's stored
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

    def get_type():
        """
        Return type for question. Text, radiobuttons, checkbox?
        Returns string
        + checkbox
        + radiobutton
        + text
        """

    def get_text(self):
        """
        Returns the question itself
        ret: string
        """

    def check_answer(self, response):
        """
        Checks if answer is correct
        """
        if response = self._answer
            return True

        return False

class RadibuttonQuestion():
    """
    Handles a radiobutton question
    """


class CheckboxQuestion():
    """
    Handles a checkbox question
    Checkboxes can have many answers
    """

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
