#!/usr/bin/python3
"""
Unittest for class City
"""
import unittest
from models.city import City


class Test_classCity(unittest.TestCase):
    """ Class that include all class City tests """

    def test_attrs(self):
        """ to check the attributes of an instances """
        city_test = City()
        self.assertEqual(city_test.state_id, "")
        self.assertEqual(city_test.name, "")

if __name__ == '__main__':
    unittest.main()
