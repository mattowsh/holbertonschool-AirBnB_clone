#!/usr/bin/python3
"""
Unittest for class State
"""
import unittest
from models.state import State


class Test_classState(unittest.TestCase):
    """ Class that include all class State tests """

    def test_attrs(self):
        """ to check the attributes of an instances """
        state_test = State()
        self.assertEqual(state_test.name, "")

if __name__ == '__main__':
    unittest.main()
