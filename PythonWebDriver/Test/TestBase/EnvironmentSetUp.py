# A base file to setup and teardown the webdriver

import unittest
import datetime
from selenium import webdriver

class EnvironmentSetup (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome ("C:\Programming\Selenium\Python Selenium\PythonWebDriver\PythonWebDriver\WebDrivers\Chrome\chromedriver.exe")
        print ("Run Started at :" + str (datetime.datetime.now()))
        print ("Chrome Environment Set Up")
        print ("------------------------------------------------------------------")
        self.driver.implicitly_wait (20)
        self.driver.maximize_window ()

    def tearDown(self):
        if (self.driver!=None):
            print ("------------------------------------------------------------------")
            print ("Test Environment Destroyed")
            print ("Run Completed at :" + str (datetime.datetime.now()))
            self.driver.close ()
            self.driver.quit ()


