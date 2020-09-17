from pages.base import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import BASE_URL

class MainPage(BasePage):

    def __init__(self):
        chop = webdriver.ChromeOptions
        chop.add_extension()



    def homePage(self):
        self.wait = WebDriverWait
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID,"startsession")))

    def start_session(self):
        browser = self.browser
        browser.find_element_by_id("startsession").click()

    def join_session(self):
        browser = self.browser
        self.wait = WebDriverWait
        browser.find_element_by_id("joinsession").click()








