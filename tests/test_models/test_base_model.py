#!/usr/bin/python3
"""
Unittest for class BaseModel methods
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import models


class Test_classBaseModel(unittest.TestCase):
    """ Class that include all class BaseModel test """

    def test_attr_types(self):
        """ to check the types of the class attributes """
        base0 = BaseModel()

        self.assertEqual(type(base0.id), str)
        self.assertEqual(type(base0.created_at), datetime)

    def test_save(self):
        """ to check the correct save of a new instance in
        JSON file """
        base2 = BaseModel()
        models.storage.save()
        with open("file.json", "r") as file:
            # calculates the length of our JSON file with one instance
            qty_words = (file.read()).split()
            before_save = len(qty_words)

        base3 = BaseModel()
        models.storage.save()
        with open("file.json", "r") as file:
            # after create a new instance, we wait the length of
            # our JSON file increment 
            qty_words = (file.read()).split()
            after_save = len(qty_words)
        
        self.assertTrue(before_save < after_save)

    def test_to_dict(self):
        """ to check the correct convertion of all attributes of an instances
        into a dictionary """
        base4 = BaseModel()
        new_dict = base4.to_dict()

        self.assertEqual(type(new_dict), dict)
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
