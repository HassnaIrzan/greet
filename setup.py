"""
@brief: This file contains the setup script for the greet package.
@author: Hassna Irzan (rmaphir@gmail.com)
@date: 24 August 2023

"""

from setuptools import setup, find_packages
from os import path

current_directory = path.abspath(path.dirname(__file__))

with open(path.join(current_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="greet",
    version="0.0.1",
    author="Hassna",
    author_email="rmaphir@gmail.com",
    license="MIT",
    description="A package to greet a person by name.",
    long_description=long_description,
    packages=['greet'],
    package_dir={'greet': 'src'},
    zip_safe=False,
)
