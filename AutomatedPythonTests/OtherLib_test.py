# Tests using pytest instead of unittest
import pytest

# Imports square class
from SquareCalc import Square
from TriangleCalc import Triangle

# Test for area of square
def test_area_square():
    sq = Square(2)
    assert sq.area() == 4

# Test for perimeter of square
def test_perimeter_square():
    sq = Square(-1)
    assert sq.perimeter() == -4

# Test for area of triangle
def test_area_triangle():
    tri = Triangle(4, 7, 8, 5, 5)
    assert tri.area() == 12.5

# Test for perimeter of triangle
def test_perimeter_triangle():
    tri = Triangle(4, 7, 8, 5, 5)
    assert tri.perimeter() == 19
