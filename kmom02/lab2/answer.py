#!/usr/bin/env python3

"""
ccf4838f1a378bb4797b038f853bfd03
oopython
lab2
v2
olai19
2020-02-06 19:44:29
v4.0.0 (2019-03-05)

Generated 2020-02-06 20:44:29 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python documentation](https://docs.python.org/3/library/index.html).
# Here you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Class relationships
#
# Practice on creating classes and relationships between them in python.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (2 points)
#
# Create a new class named **Person**.  Give the class the instance
# attributes "name" and "ssn". Make "ssn" a private attribute. The values for
# the attributes should be sent to the constructor as arguments.
# Create a *get* method for "ssn".
#
# In the code below create a new variable called **per** and set it to a new
# instance of Person. Give it the name `Skorstten` and ssn `619172-0731`.
#
#
# Answer with per\'s get method for ssn.
#
# Write your code below and put the answer into the variable ANSWER.
#
class Person():
    """
    Lab 2
    """

    def __init__(self, name, ssn, address=""):
        """
        Constructor
        """
        self.name = name
        self._ssn = ssn
        self.address = address

    def get_ssn(self):
        """
        Returns SSN
        """
        return self._ssn

    def set_address(self, address_object):
        """
        Set address
        """
        self.address = address_object

    def to_string(self):
        """
        Return string for person
        """

        ret = ("Name: " + self.name + " SSN: " + self._ssn + " " +
               self.address.to_string())

        return ret


per = Person("Skorstten", "619172-0731")


ANSWER = per.get_ssn()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (2 points)
#
# Create a new class named **Address**.  Give the class the instance
# attributes "city", "state" and "country". The values for the attributes
# should be sent to the constructor as arguments.
# Create a method, in Address, called **to_string**, it should return
# `"Address: <city> <state> <country>"` (replace the \<city\> with the value
# of the attribute city...).
#
# Add the instance attribute **address** to class Person. It's value should
# be sent as argument to constructor, give it a default value of and empty
# string, `""`.
# Create a set method for attribute "address".
# Create a method, in Person, called **to_string**, it should return `"Name:
# <name> SSN: <ssn> Address: <city> <state> <country>"`. Use Address'
# to_string method to get address data.
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Lugard`, the state `Gotland` and the country `Andor`.
# Use the set method in Person to add the newly create Address object to your
# **per** object.
#
# Answer with per's "to_string" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

class Address():
    """
    Lab2, Address
    """

    def __init__(self, city, state, country):
        """
        Constructor
        """
        self.city = city
        self.state = state
        self.country = country

    def to_string(self):
        """
        Returns string with address
        """
        ret = "Address: " + self.city + " " + self.state + " " + self.country

        return ret

place = Address("Lugard", "Gotland", "Andor")

per.set_address(place)

ANSWER = per.to_string()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (2 points)
#
# Create a new class name **Teacher** make it inherit from class "Person". In
# the constructor add the instance attribute "courses" and initiate it to and
# empty list.
# Create the method **add_course**, it should take one argument and add it to
# the course list attribute.
# Create the method **remove_course**, it should take one argument and remove
# if from the course list attribute.
# Overload the **to_string** method from the base class. It should return the
# same as the original method and add the courses to the end of the string,
# `"Name: <name> SSN: <ssn> Address: <city> <state> <country> Courses:
# <course>, <course>, ..."`. The list of courses should be comma seperated
# without one at the end. Tip, use `super(Teacher, self)` to access base
# method.
#
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Imre`, the state `Throvenland` and the country `Ceald`.
# Create a new instance of the class Teacher. Initiate it with the name
# `Buster` and ssn `768244-4857` and the aforementioned Address object.
# Use the add_course method to add the following courses, `ramverk2`,
# `python` and `javascript1`.
#
#
# Answer with the Teacher object's "to_string" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

class Teacher(Person):
    """
    Greatest of all human beings
    """
    def __init__(self, name, ssn, address=""):
        """
        Sets this person up
        """
        super().__init__(name, ssn, address)
        self.courses = []

    def add_course(self, course):
        """
        Adding courses to teachers curiculum
        """
        self.courses.append(course)

    def remove_course(self, course):
        """
        Removing courses
        """
        if course in self.courses:
            self.courses.remove()
            return True

        return False

    def to_string(self):
        """
        Returns string with address
        """
        person = Person.to_string(self)

        c = 0
        courses = ""

        while c < len(self.courses):
            courses += self.courses[c]
            if c < len(self.courses) - 1:
                courses += ", "
            c += 1

        ret = person + " Courses: " + courses

        return ret

place2 = Address("Imre", "Throvenland", "Ceald")
teacher = Teacher("Buster", "768244-4857")
teacher.set_address(place2)
teacher.add_course("ramverk2")
teacher.add_course("python")
teacher.add_course("javascript1")


ANSWER = teacher.to_string()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (2 points)
#
# Create a new class name **Student** make it inherit from class "Person". In
# the constructor add the instance attribute "courses_grades" and initiate it
# to and empty list.
# Create the method **add_course_grade**, it should take two arguments, one
# course and a grade. Create a tuple with the two arguments and add to the
# attribute "courses_grades".
# Create the method **average_grade**. Calculate and return the students
# average grade. Ignore grades with "-" in the calculation.
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Lugard`, the state `The Aiel Waste` and the country
# `Gettland`.
# Create a new instance of the class Student. Initiate it with the name
# `Hugo` and ssn `503233-4011` and the aforementioned Address object.
# Use the add_course_grade method to add the following courses, `webapp` with
# grade `4`, `ramverk2` with grade `-` and `linux` with grade `4`.
#
#
# Answer with the Student object's "average_grade" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

class Student(Person):
    """
    The lowest class of man
    """
    def __init__(self, name, ssn, address=""):
        """ Give me a student """
        super().__init__(name, ssn, address)
        self.course_grades = []

    def add_course_grade(self, course, grade):
        """ Set grades """
        self.course_grades.append((course, grade))

    def average_grade(self):
        """ Return grade average """

        grade_sum = 0
        courses = 0
        # print(self.course_grades)

        for g in self.course_grades:
            # pylint: disable=unused-variable
            course, grade = g
            if grade != "-":
                grade_sum += int(grade)
                courses += 1

        return float(grade_sum / courses)

place3 = Address("Lugard", "The Aiel Waste", "Gettland")
stud = Student("Hugo", "503233-4011", place3)

stud.add_course_grade("webapp", 4)
stud.add_course_grade("ramverk2", "-")
stud.add_course_grade("linux", "4")

ANSWER = stud.average_grade()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)


dbwebb.exit_with_summary()
