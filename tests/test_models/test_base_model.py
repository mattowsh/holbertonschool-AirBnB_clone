#!/usr/bin/python3
"""
Unittest for class BaseModel methods
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_classBaseModel(unittest.TestCase):
    """ Class that include all class BaseModel test """

    def test_attr_types(self):
        """ to check the types of the class attributes """
        base0 = BaseModel()

        self.assertEqual(type(base0.id), str)
        self.assertEqual(type(base0.created_at), datetime)
        self.assertEqual(type(base0.updated_at), datetime)

if __name__ == '__main__':
    unittest.main()
