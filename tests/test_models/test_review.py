#!/usr/bin/python3
"""
Unittest for class Review
"""
import unittest
from models.review import Review


class Test_classReview(unittest.TestCase):
    """ Class that include all class Review tests """

    def test_attrs(self):
        """ to check the attributes of an instances """
        review_test = Review()
        self.assertEqual(review_test.place_id, "")
        self.assertEqual(review_test.user_id, "")
        self.assertEqual(review_test.text, "")

if __name__ == '__main__':
    unittest.main()
