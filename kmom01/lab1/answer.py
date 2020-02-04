#!/usr/bin/env python3

"""
d10bd74e2bd150e7b1f616dd18ba2cda
oopython
lab1
v2
olai19
2020-02-02 17:04:31
v4.0.0 (2019-03-05)

Generated 2020-02-02 18:04:31 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb
from classes import Cat, Duration

# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 1 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python documentation](https://docs.python.org/3/library/index.html).
# Here you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Objects and classes
#
# Basic object oriented python.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a new file, put your code for the classes in it, call it
# **classes.py**. In classes.py create the class Cat. Add the following
# instance attributes in the Cat class constructor:
# - `eye_color`
# - `name`
# Add a paramater for each attribute in the constructor definition.
#
# Dont forget to import the file!
#
# In the code below create a new variable called `cat1` and initiate it with
# a new *Cat object*.
# Give the object the eye color "green" and the name "Misha".
#
# Answer with the string "My cats name is `name` and has `eye_color` eyes.".
#
# Write your code below and put the answer into the variable ANSWER.
#

cat1 = Cat()

cat1.eye_color = 'green'
cat1.name = 'Misha'


ANSWER = ("My cats name is " + cat1.name + " and has " +
          cat1.eye_color + " eyes.")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Expand your Cat class with the private instance attribute `lives_left`.
# Also add a *set*- and *get*-method for the attribute.
# In the constructor, give `lives_left` a default value of `-1` if no other
# value is sent to the constructor.
#
# In the code below use the set-method on cat1 to change the value to `7`.
#
# Use the get method to answer with how many lives cat1 has left.
#
# Write your code below and put the answer into the variable ANSWER.
#

cat1.set_lives_left(7)


ANSWER = cat1.get_lives_left()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a new method in the Cat class, called `description`. The method
# should return the string "My cats name is `name`, has `eye_color` eyes and
# `lives_left` lives left to live.". Use `self` to access the values for each
# attribute (in the description method).
#
# Answer with the result returned from `cat1.description()`.
#
# Write your code below and put the answer into the variable ANSWER.
#



# print(cat1.description())


ANSWER = cat1.description()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a static attribute in the Cat class, "nr_of_paws", that contains the
# number of paws a cat have.
# Assign its value to `4` in the declaration.
#
# Answer with the string "`cat1.name` has `cat1.nr_of_paws` paws.".
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = cat1.name + " has " + str(cat1.nr_of_paws) + " paws."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# In the code below assign `1` to cat1's nr_of_paws.
#
# Answer with the string "`cat1.name` has `cat1.nr_of_paws` paws but cats
# have `Cat.nr_of_paws` paws.".
#
# Write your code below and put the answer into the variable ANSWER.
#

cat1.nr_of_paws = 1


ANSWER = (cat1.name + " has " + str(cat1.nr_of_paws) + " paws but cats have " +
          str(Cat.nr_of_paws) + " paws.")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a new variable called `cat2` and initiate it with a new Cat objekt.
# Give cat2 the name "Nynaeve" and eye color "blue".
#
# Put cat1 and cat2 variables in a list. Iterate through the list and
# concatenate the result from their description methods together in a string,
# with a space seperation the two strings.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

cat2 = Cat()

cat2.name = "Nynaeve"
cat2.eye_color = "blue"

cat_list = [cat1, cat2]

i = 0
cat_str = ''

while i < len(cat_list):
    # print(cat_list[i].description())
    cat_str += cat_list[i].description()
    if i < len(cat_list) - 1:
        cat_str += " "
    i += 1

# print(cat_str)

ANSWER = cat_str


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a new class named Duration.
# Declare the following instance attributes in the constructor:
# - `hours`
# - `minutes`
# - `seconds`
# Add a parameter for each attribute to the method heading and assign each
# parameter to respective attribute.
#
# Add the method `display` to the class, it should return the duration as a
# string with the format "hh-mm-ss".
# Numbers below 10 should have a leading zero in the string.
#
# Initialize a new *Duration object* and assign it to a variable called
# `duration1`. Give it hours `26`, minutes `5` and seconds `20`.
#
# Answer with the result from the display method.
#
# Write your code below and put the answer into the variable ANSWER.
#

duration1 = Duration(26, 5, 20)




ANSWER = duration1.display()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.8 (1 points)
#
# Create a static method in the Duration class, name it `duration_to_sec`.
# The method should take one argument, a string in the format as the one
# `display` returns, "hh-mm-ss".
# The method should return the duration it represents converted to number of
# seconds.
#
# Answer with `Duration.duration_to_sec(duration1.display())`.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = Duration.duration_to_sec(duration1.display())

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.8", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Overriding methods
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Overload the `add operator(+)` in the Duration class.
# It should return the duration of two objects added together, in seconds.
#
# Initialize a new Duration object to a variable called `duration2` , give it
# hours `27`, minutes `31` and seconds `8`.
#
# Answer with `duration1+duration2`.
#
# Write your code below and put the answer into the variable ANSWER.
#

duration2 = Duration(27, 31, 8)

# print(duration1.duration_to_sec(duration1.display()))
# print(duration2.duration_to_sec(duration2.display()))
#
# print(duration2 + duration1)


ANSWER = duration1 + duration2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Overload the `iadd operator(+=)` in the Duration class to update the own
# object with the sum of its own units and the other objects units,
# hours+other.hours, minutes+other.minutes and seconds+other.seconds.
#
# Initialize a new Duration object to a variable called `duration3` , give it
# hours `9`, minutes `31` and seconds `43`.
# In the code use "+=" to update `duration2` with `duration3`.
#
# Answer with `duration2`s display method.
#
# Write your code below and put the answer into the variable ANSWER.
#

# print(duration2.display())

duration3 = Duration(9, 31, 43)
duration2 += duration3

# print(duration2.display())


ANSWER = duration2.display()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Overload the `smaller than operator(<)` in the Duration class.
# It should return True if the duration is shorter than the other.
#
# Answer with `duration1<duration2`.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)


dbwebb.exit_with_summary()
