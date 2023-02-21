import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    
    def test_add(self):
        
        # Arrange
        inputA = 5
        inputB = 6
        expected = 11
        
        # Act
        actual = Calculator.add(inputA, inputB)
        
        # Assert
        self.assertEqual(expected, actual)
