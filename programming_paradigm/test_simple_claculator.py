import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class."""

    def setUp(self):
        """Set up the calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition operation with various inputs."""
        # Test positive integers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative integers
        self.assertEqual(self.calc.add(-1, -1), -2)
        # Test mixed positive/negative
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Test with zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)
        # Test large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

    def test_subtraction(self):
        """Test subtraction operation with various inputs."""
        # Test positive integers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative integers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        # Test mixed positive/negative
        self.assertEqual(self.calc.subtract(1, -1), 2)
        # Test with zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.1), 3.4)
        # Test large numbers
        self.assertEqual(self.calc.subtract(2000000, 1000000), 1000000)

    def test_multiplication(self):
        """Test multiplication operation with various inputs."""
        # Test positive integers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # Test negative integers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        # Test with zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)
        # Test identity
        self.assertEqual(self.calc.multiply(5, 1), 5)
        # Test large numbers
        self.assertEqual(self.calc.multiply(1000, 2000), 2000000)

    def test_division(self):
        """Test division operation with various inputs."""
        # Test normal division
        self.assertEqual(self.calc.divide(6, 3), 2)
        # Test negative numbers
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(6, -3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        # Test floating point results
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        # Test zero divided by non-zero
        self.assertEqual(self.calc.divide(0, 5), 0)
        # Test floating point inputs
        self.assertAlmostEqual(self.calc.divide(5.5, 2), 2.75)
        # Test large numbers
        self.assertEqual(self.calc.divide(2000000, 1000000), 2)

if __name__ == '__main__':
    unittest.main()