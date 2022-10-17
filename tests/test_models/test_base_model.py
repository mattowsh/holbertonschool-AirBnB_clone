#!/usr/bin/python3
"""
Unittest for class BaseModel methods
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
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

    def test_to_dict(self):
        """ to check the correct convertion of all attributes of an instances
        into a dictionary """
        base4 = BaseModel()
        new_dict = base4.to_dict()

        self.assertEqual(type(new_dict), dict)
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)

    def test_str(self):
        model = BaseModel()
        prin = f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}"
        self.assertEqual(prin, model.__str__())

    def test_save(self):
        storage = FileStorage()
        storage.all().clear()
        my_model = BaseModel()
        try:
            os.remove("file.json")
        except Exception:
            pass
        my_model.save()
        self.assertTrue(os.path.exists("file.json"))

if __name__ == '__main__':
    unittest.main()
