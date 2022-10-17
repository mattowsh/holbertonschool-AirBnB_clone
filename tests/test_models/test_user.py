#!/usr/bin/python3
"""
Unittest for class User methods
"""
import unittest
from models.user import User
from datetime import datetime


class Test_classUser(unittest.TestCase):
    """ Class that include all class BaseModel test """

    def test_attr1(self):
        """ to check the attributes of an instances: email and password """
        testclass = User(email="hbnh@mail.com", password="root")
        self.assertEqual(testclass.email, "hbnh@mail.com")
        self.assertEqual(testclass.password, "root")

    def test_attr2(self):
        """ to check the attributes of an instances: first_name
        and last_name """
        testclass2 = User(first_name="Jimmy", last_name="Neutron")
        self.assertEqual(testclass2.first_name, "Jimmy")
        self.assertEqual(testclass2.last_name, "Neutron")
