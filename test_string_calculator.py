
import unittest
from string_calculator import add

class TestStringCalculator(unittest.TestCase):
    #  add test for empty string
    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    # add test for one number
    def test_one_number(self):
        self.assertEqual(add("1"), 1)
        
    # add test for two numbers
    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)
