# This module contains DuckDuckGoSearchPage
# The page object for the DuckDuckGo Search Page


class DuckDuckGoSearchPage:
    
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    
    def __init__(self,browser):             #contractor
        self.browser = browser
        
    def load(self):                         #method to load the page
        #TODO
        pass
    
    def search(self,phrase):                #method for search
        #TODO
        pass
    