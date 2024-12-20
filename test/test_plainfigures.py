import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hw5_lib', 'hw5_lib')))

sys.path.append(os.path.abspath("../"))  
from hw5 import Triangle, Rectangle, Circle

def test_triangle():
    triangle = Triangle(3, 4, 5, 4)
    assert triangle.compute_perimeter() == 12
    assert triangle.compute_surface() == 6

def test_rectangle():
    rectangle = Rectangle(3, 4)
    assert rectangle.compute_perimeter() == 14
    assert rectangle.compute_surface() == 12

def test_circle():
    circle = Circle(2)
    assert pytest.approx(circle.compute_perimeter(), 0.001) == 12.5664
    assert pytest.approx(circle.compute_surface(), 0.001) == 12.5664
