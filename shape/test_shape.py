from unittest import TestCase
from math import pi
from shape import shape

class Test(TestCase):
    def test_get_area(self):
        self.assertEqual(shape.get_area(1), pi)
        self.assertEqual(shape.get_area(0), None)
        self.assertEqual(shape.get_area(-2), None)
        self.assertEqual(shape.get_area("10"), None)
        self.assertEqual(shape.get_area(3, 4, 5), 3 * 4 / 2)

    def test_is_right_triangle(self):
        self.assertEqual(shape.is_right_triangle(3, 4, 5), True)
        self.assertEqual(shape.is_right_triangle(3, 4, 7), False)
        self.assertEqual(shape.is_right_triangle(3, 4, 7, 10), None)
        self.assertEqual(shape.is_right_triangle(3, 4), None)
        self.assertEqual(shape.is_right_triangle(3), None)
        self.assertEqual(shape.is_right_triangle(3.0, 4.0, 5.0), True)
        self.assertEqual(shape.is_right_triangle(3, 4, "5"), None)
