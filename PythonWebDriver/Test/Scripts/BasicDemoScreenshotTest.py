### Basic Demo ###

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("C:/Users/Solomon/git/PythonWebDriver/PythonWebDriver/WebDrivers/Chrome/chromedriver.exe")
#webdriver.FirefoxBinary("C:\Programming\Selenium\Python Selenium\PythonWebDriver\PythonWebDriver\WebDrivers\FireFox\geckodriver.exe")
#webdriver.InternetExplorer("C:\Programming\Selenium\Python Selenium\PythonWebDriver\PythonWebDriver\WebDrivers\InternetExplorer\IEDriverServer.exe")

driver.set_page_load_timeout(20)
driver.get("http://newtours.demoaut.com/")

driver.get_screenshot_as_file("C:\Programming\Selenium\Python Selenium\PythonWebDriver\PythonWebDriver\Screenshot\Home.png")    #Tacking a screenshot need to give location and file name

print(driver.title)
driver.implicitly_wait(10)
sleep(4)

print("Test completed")

driver.close()
driver.quit()