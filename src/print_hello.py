"""
@brief: This file contains a class that prints a greetings given the name of a person.
@file: print_hello.py
@date: 2020-06-27
@version: 0.0.1
@author: Hassna Irzan (rmaphir@gmail.com)

"""


# make a class that prints a greetings
class GreetPerson:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello " + self.name + "!")

