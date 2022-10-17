#!/usr/bin/python3
"""
Unittest for class Amenity
"""
import unittest
from models.amenity import Amenity


class Test_classAmenity(unittest.TestCase):
    """ Class that include all class Amenity tests """

    def test_attrs(self):
        """ to check the attributes of an instances """
        amenity_test = Amenity()
        self.assertEqual(amenity_test.name, "")

if __name__ == '__main__':
    unittest.main()
