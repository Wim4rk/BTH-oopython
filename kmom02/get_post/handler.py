#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Handler file for Employee
"""

from employee import Employee

class Handler():
    """Handler class"""
    def __init__(self):
        self.people = []
        self.add_predefined_employees()

    def get_people(self):
        """Returns employees"""
        return self.people

    def add_employee(self, form):
        """Process form data"""
        empl = Employee(
            form["firstname"],
            form["lastname"],
            form["salary"]
        )
        self.people.append(empl)

    def write_session(self, session):
        """
        Save state to session
        """
        session["employees"] = [e.to_json() for e in self.people]

    def read_session(self, session):
        """
        Get state from session
        """
        if session.get("employees", []):
            self.people = [Employee.from_json(e) for e in session["employees"]]

    def add_predefined_employees(self):
        """Hardcoded persons"""
        emil = Employee("Emil", "Folino", 30000)
        mikael = Employee("Mikael", "Roos", 31000)
        kenneth = Employee("Kenneth", "Lewenhagen", 75000)
        andreas = Employee("Andreas", "Arnesson", 12000)

        self.people.append(emil)
        self.people.append(mikael)
        self.people.append(kenneth)
        self.people.append(andreas)
