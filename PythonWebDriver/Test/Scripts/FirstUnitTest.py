### Demo for using a base script to setup and tear down the webdriver ###
###This file is using TestBase->EnvironmentSetUp

from datetime import datetime
from selenium import webdriver
from time import sleep
import unittest
from Test.TestBase.EnvironmentSetUp import EnvironmentSetup                     #Importing the function from the test base

class MyTestCase (EnvironmentSetup):

    # def setUp(self):                    #A function that is creating the driver
    #     self.driver = webdriver.Chrome ("C:\Programming\Selenium\Python Selenium\PythonWebDriver\PythonWebDriver\WebDrivers\Chrome\chromedriver.exe")
    #     self.driver.implicitly_wait (10)
    #     self.driver.set_page_load_timeout(20)
    #     print ("---------------------")
    #     print ("Test Enviroment Created")
    #     print ("Run Started at : " + str (datetime.now()))


    def test_NavigateMercury(self):     #A function that is navigating to a website and tacking a screenshot
        driver = self.driver
        self.driver.get("http://newtours.demoaut.com/")
        self.driver.get_screenshot_as_file ("C:\Programming\Selenium\Python Selenium\PythonWebDriver\PythonWebDriver\Screenshot\Home1.png")
        print (self.driver.title)
        sleep (4)
        print ("Test completed")


    # def tearDown(self):             #A function that is destroying the driver
    #     if (self.driver!=None):
    #         print("---------------------")
    #         print("Test Enviroment Destroyed")
    #         print("Run Completed at : "+ str(datetime.now()))
    #         self.driver.close()
    #         self.driver.quit


if __name__ == '__main__':
    unittest.main ( )
