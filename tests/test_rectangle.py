"""
test functions of Rectangle()

zs. elter 2019
"""

import unittest
from feign.geometry import *

class TestRectangleDefinition(unittest.TestCase):
    def test_rectangle_wrong_corner_order(self):
        with self.assertRaises(ValueError):
            rect=Rectangle(Point(3,7),Point(13,5),Point(5,3),Point(12,6))
    def test_rectangle_concave_shape(self):
        with self.assertRaises(ValueError):
            rect=Rectangle(Point(5,3),Point(13,5),Point(10,7),Point(10,10))


class TestEnclosesPoint(unittest.TestCase):
    def test_encloses_point_yes(self):
        rect=Rectangle(Point(3,7),Point(5,3),Point(13,5),Point(12,6))
        self.assertTrue(rect.encloses_point(Point(6,5)))
    def test_encloses_point_no(self):
        rect=Rectangle(Point(3,7),Point(5,3),Point(13,5),Point(12,6))
        self.assertFalse(rect.encloses_point(Point(4,3)))

#class TestRectIntersection(unittest.TestCase):

if __name__ == '__main__':
    unittest.main()

