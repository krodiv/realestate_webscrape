import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

class Scraper:
    def __init__(self):
        self.driver = None

    def create_driver(self, driver_type=None):
        if driver_type:
            pass
            #set given driver type
        else:
            #set firefox as standard driver
            self.driver = webdriver.Firefox()
        return 

    def get_source(self, source):
        #do something here for setting up a source
        self.driver.get(source)
        return self.driver
