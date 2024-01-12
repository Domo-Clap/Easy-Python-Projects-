# Imports unittest library
import unittest

# Imports square class
from SquareCalc import Square

# Extends the unittest library to use test cases
class TestSquare(unittest.TestCase):

    # Defines a basic value to use for all tests
    def setUp(self):
        self.calc = Square(10)

    # Test for area of square
    def test_area(self):
        self.assertEqual(self.calc.area(), 100)

    # Test for perimeter of square
    def test_perimeter(self):
        self.assertEqual(self.calc.perimeter(), 40)

if __name__ == '__main__':
    # Calls the unit tests
    unittest.main()