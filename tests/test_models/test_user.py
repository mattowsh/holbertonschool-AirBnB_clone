#!/usr/bin/python3
"""
Unittest for class User
"""
import unittest
from models.user import User


class Test_classUser(unittest.TestCase):
    """ Class that include all class BaseModel test """

    def test_attrs(self):
        """ to check the attributes of an instances """
        usertest = User()
        self.assertEqual(usertest.email, "")
        self.assertEqual(usertest.password, "")
        self.assertEqual(usertest.first_name, "")
        self.assertEqual(usertest.last_name, "")

if __name__ == '__main__':
    unittest.main()
