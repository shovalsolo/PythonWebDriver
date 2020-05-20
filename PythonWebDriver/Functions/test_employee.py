# A unittest file that is testing employee.py methods

import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):

    @classmethod                                                        #
    def setUpClass(cls):                                                #This will run only one time in the beginning of the class
        print('setUpClass')

    @classmethod                                                        #
    def tearDownClass(cls):                                             #This will run only one time in the end of the class
        print('tearDownClass')

    def setUp(self):                                                    #Will run before every test
        print('setUp')
        self.emp1 = Employee('Corey','Schafer',50000)                   #creating emp1 before every test
        self.emp2 = Employee('Sue', 'Smith', 60000)                     #creating emp2 before every test

    def tearDown(self):                                                 #Will run after every test
        print ('tearDown\n')

    def test_email(self):                                               #Test case to check the email method
        print ('test_email')
        # emp1 = Employee('Corey', 'Schafer', 50000)                    #Removed because created in the setUp
        # emp2 = Employee('Sue', 'Smith', 60000)                        #Removed because created in the setUp

        self.assertEqual(self.emp1.email, 'Corey.Schafer@email.com')    #Checking that the email was created correctly to the names given
        self.assertEqual(self.emp2.email, 'Sue.Smith@email.com')        #Checking that the email was created correctly to the names given

        self.emp1.first = 'John'                                        #Changing the first name for the first employee
        self.emp2.first = 'Jane'                                        #Changing the first name for the second employee

        self.assertEqual(self.emp1.email, 'John.Schafer@email.com')     #Checking that the email was created correctly to the new first names given
        self.assertEqual(self.emp2.email, 'Jane.Smith@email.com')       #Checking that the email was created correctly to the new first names given


    def test_fullname(self):                                            #Test case to check the full name method
        print ('test_fullname')
        # emp1 = Employee('Corey', 'Schafer', 50000)                    #Removed because created in the setUp
        # emp2 = Employee('Sue', 'Smith', 60000)                        #Removed because created in the setUp

        self.assertEqual(self.emp1.fullname, 'Corey Schafer')           #Checking that the full name was created correctly to the new first and last names given
        self.assertEqual(self.emp2.fullname, 'Sue Smith')               #Checking that the full name was created correctly to the new first and last names given

        self.emp1.first = 'John'                                        #Changing the first name for the first employee
        self.emp2.first = 'Jane'                                        #Changing the first name for the second employee

        self.assertEqual(self.emp1.fullname, 'John Schafer')            #Checking that the full name was created correctly to the new first names given
        self.assertEqual(self.emp2.fullname, 'Jane Smith')              #Checking that the full name was created correctly to the new first names given


    def test_apply_raise(self):                                         #Test case to check the apply rise method
        print ('test_apply_raise')
        # self.emp1 = Employee('Corey', 'Schafer', 50000)               #Removed because created in the setUp
        # self.emp2 = Employee('Sue', 'Smith', 60000)                   #Removed because created in the setUp

        self.emp1.apply_raise()                                         #Applying a rise on employee1
        self.emp2.apply_raise()                                         #Applying a rise on employee1

        self.assertEqual(self.emp1.pay, 52500)                          #Checking the a rise og 5% was given on the salary
        self.assertEqual(self.emp2.pay, 63000)                          #Checking the a rise og 5% was given on the salary


    def test_monthly_schedule(self):                                #Test case to check the test monthly schedule method
        print ('monthly_schedule')
        with patch('employee.requests.get') as mocked_get:          #
            mocked_get.return_value.ok = True                       #Setting return value ok to True
            mocked_get.return_value.text = 'Success'                #Setting return value text to Success

            schedule = self.emp1.monthly_schedule('May')            #Setting schedule to month May
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')                   #Checking if the return is equal to Success


            mocked_get.return_value.ok = False                      #Setting return value ok to True

            schedule = self.emp2.monthly_schedule ('June')          #Setting schedule to month June
            mocked_get.assert_called_with ('http://company.com/Smith/June')
            self.assertEqual (schedule, 'Bad Response!')                  #Checking if the return is equal to Bad Response!


if __name__=='__main__':                                                #adding this line to be able to run tbe test from the ide and not from cmd
    unittest.main()                                                     #usind unittest.main to run the test

