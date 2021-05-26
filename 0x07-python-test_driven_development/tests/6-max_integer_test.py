#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for '6-max_integer.py' """
    def test_number_cases(self):
        """Number cases"""
        self.assertEqual(max_integer([-2, -1, -3]), -1)
        self.assertEqual(max_integer([6, 4, 7, 2]), 7)
        self.assertEqual(max_integer([-2, 3, -5, 1]), 3)
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([5]), 5)

    def test_float(self):
        """Test for floats"""
        self.assertEqual(max_integer([2.3, 3.2, 4.4, 5.1]), 5.1)
        self.assertEqual(max_integer([-16.5, -21.32, -1.5, -1.85]), -1.5)

    def test_string(self):
        """Test strings"""
        self.assertEqual(max_integer("1, 2, 3"), "3")

    def test_empty_list(self):
        """Empty list case"""
        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()
