# This module contains DuckDuckGoResultPage
# The page object for the DuckDuckGo Search Result Page

from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
    
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')
    
    def __init__(self,browser):             #contractor
        self.browser = browser
        
    def result_link_titles(self):           #method to load the page
        #TODO
        return[]
    
    def search_input_value(self):          #method for search
        #TODO
        return ""
    
    
    def title(self):                        #method for search
        #TODO
        return ""