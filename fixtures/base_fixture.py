from selenium import webdriver
import unittest

from pages.login_page import LoginPage
from tests import CHROME_DRIVER


class fixtures(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_DRIVER)
        self.login_page = LoginPage(self.browser)
        self.login_page.go_to_page()


    def tearDown(self) -> None:
        self.browser.quit()
