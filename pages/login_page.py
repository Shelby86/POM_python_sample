from pages.base import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import BASE_URL


class LoginPage(BasePage):
    def __init__(self,browser):
        super().__init__(browser)


    def login(self):
        browser = self.browser
        self.wait = WebDriverWait(browser,20)
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID,"profile_username")))
        browser.find_element_by_id("profile_username").send_keys("Shelby")
        browser.find_element_by_id("getstarted").click()


        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "startsession")))

    def go_to_page(self):
        self.browser.get(BASE_URL)

