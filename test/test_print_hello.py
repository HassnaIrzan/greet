"""
@brief: Unit test to check the greet package.
@author: Hassna Irzan (rmaphir@gmail.com)
@date: 24 August 2023
"""

import unittest
import greet


class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet.GreetPerson("Hassna").greet(), "Hello Hassna!")

    def test_greet_type(self):
        with self.assertRaises(TypeError):
            greet.GreetPerson(1).greet()
            greet.GreetPerson(1.0).greet()
            greet.GreetPerson([1, 2, 3]).greet()
            greet.GreetPerson({"name": "Hassna"}).greet()


if __name__ == '__main__':
    unittest.main()
