# %%

pip install pytest

sys.path.append(os.path.abspath("../hw5_lib"))  
from hw5_lib.hw5 import plain_figures

import unittest
from plane_figures import Triangle, Rectangle, Circle

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

# Test for invalid input (optional)
def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(-1, 2, 3, 4)
