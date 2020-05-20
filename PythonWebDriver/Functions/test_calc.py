# A unittest file that is testing calc.py file
# To run the test run cmd fron the file directory
# C:\Programming\Selenium\Python Selenium\PythonWebDriver\PythonWebDriver\Functions
# And run the following command
# python -m unittest test_calc.py

import unittest
import calc

class TestCalc(unittest.TestCase):                      #creating a class tha is inhareting functionality from unittest.TestCase to create test cases

    def test_add(self):                                 # The test is checking the add method - it has to start with the word test_name of method
        result = calc.add(10,5)                         # Saving to result and calling the function with 2 numbers
        self.assertEqual(result,15)                     # Checking if the result is equal to the number we want
        self.assertEqual (calc.add(-1,1), 0)            # Checking if the result is equal to the number we want
        self.assertEqual (calc.add(-1,-1), -2)          # Checking if the result is equal to the number we want

    def test_subtract(self):                            # The test is checking the subtract method
        self.assertEqual (calc.subtract(10,5), 5)       # Checking if the result is equal to the number we want
        self.assertEqual (calc.subtract (-1, 1), -2)    # Checking if the result is equal to the number we want
        self.assertEqual (calc.subtract (-1, -1), 0)    # Checking if the result is equal to the number we want

    def test_multiply(self):                            # The test is checking the add method - it has to start with the word test_name of method
        self.assertEqual(calc.multiply(10,5),50)        # Checking if the result is equal to the number we want
        self.assertEqual (calc.multiply(-1,1), -1)      # Checking if the result is equal to the number we want
        self.assertEqual (calc.multiply(-1,-1), 1)      # Checking if the result is equal to the number we want

    def test_divide(self):                              # The test is checking the add method - it has to start with the word test_name of method
        self.assertEqual(calc.divide(10,5),2)           # Checking if the result is equal to the number we want
        self.assertEqual (calc.divide(-1,1), -1)        # Checking if the result is equal to the number we want
        self.assertEqual (calc.divide(-1,-1), 1)        # Checking if the result is equal to the number we want

        #self.assertEqual (calc.divide (-1, 0), 1)      # Checking if the result is equal to the number we want
        self.assertRaises(ValueError, calc.divide,10,0) # Checking the ValueError for dividing by zero

if __name__=='__main__':                        #adding this line to be able to run tbe test from the ide and not from cmd
    unittest.main()                             #usind unittest.main to run the test
