# %%
import unittest
from plane_figures import Triangle, Rectangle, Circle

class TestPlaneFigures(unittest.TestCase):

    def test_triangle(self):
        triangle = Triangle(3, 4, 5, 4)
        self.assertEqual(triangle.compute_perimeter(), 12)
        self.assertEqual(triangle.compute_surface(), 6)

    def test_rectangle(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.compute_perimeter(), 14)
        self.assertEqual(rectangle.compute_surface(), 12)

    def test_circle(self):
        circle = Circle(2)
        self.assertAlmostEqual(circle.compute_perimeter(), 12.5664, places=4)
        self.assertAlmostEqual(circle.compute_surface(), 12.5664, places=4)

if __name__ == '__main__':
    unittest.main()


