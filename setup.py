from setuptools import setup, find_packages
from os import path

current_directory = path.abspath(path.dirname(__file__))

with open(path.join(current_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="greetperson",
    version="0.1",
    author="Hassna",
    author_email="rmaphir@gmail.com",
    license="MIT",
    description="A package to greet a person by name.",
    long_description=long_description,
    packages=['greetperson'],
    zip_safe=False,
)
