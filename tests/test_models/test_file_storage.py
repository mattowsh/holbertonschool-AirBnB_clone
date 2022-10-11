#!/usr/bin/python3
"""
Unittest for class FileStoreage methods
"""
import unittest
from models.engine.file_storage import FileStorage
from models.engine.__init__ import __init__


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

if __name__ == '__main__':
    unittest.main()
