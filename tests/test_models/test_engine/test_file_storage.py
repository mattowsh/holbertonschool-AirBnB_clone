#!/usr/bin/python3
"""
Unittest for class FileStoreage methods
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class Test_classFileStorage(unittest.TestCase):
    """ Class that includes all class FileStorage tests """

    def test_file_path(self):
        """ to check the private attribute __file_path """
        testclass = FileStorage()
        self.assertEqual(testclass._FileStorage__file_path, 'file.json')
        # Syntax: bc __file_path and __objects are private attributes
        # of the FileStorage class

    def test_objects(self):
        """ to check the private attribute __objects """
        testclass = FileStorage()
        self.assertEqual(type(testclass._FileStorage__objects), dict)

    def test_all(self):
        storage = FileStorage()
        self.assertEqual(type(storage.all()), dict)

    def test_new(self):
        my_model = BaseModel()
        storage = FileStorage()
        storage.new(my_model)
        prin = f"{my_model.__class__.__name__}.{my_model.id}"
        self.assertEqual(storage.all()[prin], my_model)

    def test_save(self):
        storage = FileStorage()
        storage.all().clear()
        my_model = BaseModel()
        storage.save()
        self.assertNotEqual(len(storage.all()), 0)

    def test_reload(self):
        storage = FileStorage()
        storage.all().clear()
        storage.reload()
        self.assertNotEqual(len(storage.all()), 0)

if __name__ == '__main__':
    unittest.main()
