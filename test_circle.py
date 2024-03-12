"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
from math import pi


class CircleTest(unittest.TestCase):
    """Test of Circle Class."""
    def test_add_area_with_typical_value(self):
        """Test adding two circle create new circle with correct radius and area."""
        c1 = Circle(4)
        c2 = Circle(3)
        new_c = c1.add_area(c2)
        expected_radius = 5
        expected_area = pi*new_c.get_radius()*new_c.get_radius()
        self.assertEqual(expected_radius, new_c.get_radius())
        self.assertEqual(expected_area, new_c.get_area())

    def test_add_area_edge_case(self):
        """Test adding circle with non-zero radius and
        circle with zero radius.
        """
        c1 = Circle(4)
        c2 = Circle(0)
        new_c = c1.add_area(c2)
        self.assertEqual(new_c.get_radius(), c1.get_radius())
        self.assertEqual(new_c.get_area(), c1.get_area())

    def test_create_circle_with_negative_radius(self):
        """Test contrsucting Circle with negative radius should raise error."""
        with self.assertRaises(ValueError):
            negative_c = Circle(-5)
