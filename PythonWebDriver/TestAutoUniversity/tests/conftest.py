# These module contains shared fixtures and the information to the webddriver

import pytest
import selenium.webdriver



@pytest.fixture
def browser():
    
    # Initialize the ChreomeDriver instance
    b = selenium.webddriver.Chrome('C:/Users/Solomon/git/PythonWebDriver/PythonWebDriver/WebDrivers/Chrome/chromedriver.exe')
    
    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(10)
    
    #Open URL
    b.get("http://newtours.demoaut.com/")
    
    # Return the WenDriver instance for the setup 
    yield b
    
    # Quit the WebDriver instance for cleanup'
    b.quit()
    