from tests import BASE_URL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# The base url is in the tests __init__ file
# so from tests get this value

import unittest

class BasePage(object):
    def __init__(self, browser):
        self.browser = browser


        self.PAGE_URI = ""

    def get_title(self) -> str:
        return self.browser.find_element_by_css_selector(".head h1").text

    def go_to_page(self):
        self.browser.get(BASE_URL + self.PAGE_URI)