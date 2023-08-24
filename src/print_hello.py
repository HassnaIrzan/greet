"""
@brief: This file contains a class that prints a greetings given the name of a person.
@file: print_hello.py
@date: 24 August 2023
@version: 0.0.1
@author: Hassna Irzan (rmaphir@gmail.com)

"""


# make a class that prints a greetings
class GreetPerson:
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name must be a string.")

    def greet(self):
        return "Hello " + self.name + "!"

