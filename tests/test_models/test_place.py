#!/usr/bin/python3
"""
Unittest for class Place
"""
import unittest
from models.place import Place


class Test_classPlace(unittest.TestCase):
    """ Class that include all class Place tests """

    def test_attrs(self):
        """ to check the attributes of an instances """
        place_test = Place()
        self.assertEqual(place_test.city_id, "")
        self.assertEqual(place_test.user_id, "")
        self.assertEqual(place_test.name, "")
        self.assertEqual(place_test.description, "")
        self.assertEqual(place_test.number_rooms, 0)
        self.assertEqual(place_test.number_bathrooms, 0)
        self.assertEqual(place_test.max_guest, 0)
        self.assertEqual(place_test.price_by_night, 0)
        self.assertEqual(place_test.latitude, 0.0)
        self.assertEqual(place_test.longitude, 0.0)
        self.assertEqual(place_test.amenity_ids, [])

if __name__ == '__main__':
    unittest.main()
