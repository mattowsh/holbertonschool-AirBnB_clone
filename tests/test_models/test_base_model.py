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

    #def test_save(self):
     #   """ to check the correct update of updated_at attribute """
      #  base1 = BaseModel()
        
        # we save the actual value
       # old_value = base1.__dict__["updated_at"]

        # update the value and save
        #models.storage.save()

        # check if the old_value == updated value
        #self.assertNotEqual(base1.__dict__["updated_at"], old_value)

    def test_to_dict(self):
        """ to check the correct convertion of all attributes of an instances
        into a dictionary """
        base4 = BaseModel()
        new_dict = base4.to_dict()

        self.assertEqual(type(new_dict), dict)
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)

if __name__ == '__main__':
    unittest.main()
