import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self):
        self.driver = None
        self.soup = None

    def create_driver(self, driver_type=None):
        #For selenium use
        if driver_type:
            pass
            #set given driver type
        else:
            #set firefox as standard driver
            self.driver = webdriver.Firefox()
        return 

    def get_source(self, source):
        #get website via selenium
        self.driver.get(source)
        return self.driver

    def find_element_by_class_name(self, element_name):
        #get website element with selenium
        content = self.driver.find_element(By.CLASS_NAME, element_name)
        return content

    # the below are not using selenium
    # requests along with beautiful soup is used
    def get_website_text(self, url):
        #get website content via requests
        return requests.get(url).text

    def init_bs4(self, url):
        #initalize beautiful soup object
        text = self.get_website_text(url)
        self.soup = BeautifulSoup(text, "html.parser")

    def find_sb4(self, tag_type, class_name):
        tag_list = self.soup.find_all(tag_type, class_name)
        return tag_list