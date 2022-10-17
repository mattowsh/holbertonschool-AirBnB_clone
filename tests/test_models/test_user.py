#!/usr/bin/python3
"""
Unittest for class User
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class Test_classUser(unittest.TestCase):
    """ Class that include all class BaseModel test """

    def test_email(self):
        """ to check the attribute of an instances: email """
        user0 = User(email="hbnh@mail.com")
        self.assertEqual(user0.email, "hbnh@mail.com")

    def test_password(self):
        """ to check the attribute of an instances: password """
        user1 = User(password="root")
        self.assertEqual(user1.password, "root")

    def test_firstname(self):
        """ to check the attribute of an instances: first_name """
        user2 = User(first_name="Jimmy")
        self.assertEqual(user2.first_name, "Jimmy")

    def test_lastname(self):
        """ to check the attribute of an instances: last_name """
        user3 = User(last_name="Neutron")
        self.assertEqual(user3.last_name, "Neutron")
