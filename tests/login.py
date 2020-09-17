import unittest
from selenium import webdriver

from pages.login_page import LoginPage
from tests import CHROME_DRIVER


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path=CHROME_DRIVER)
        self.login_page = LoginPage(self.browser)
        self.login_page.go_to_page()

    def tearDown(self) -> None:
        self.browser.quit()


    def test_something(self):
        self.login_page = LoginPage(self.browser)
        self.login_page.login()

        welcome_message = self.browser.find_element_by_xpath("//span[text()='Welcome']")

        self.assertTrue(welcome_message.is_displayed())

if __name__ == '__main__':
    unittest.main()
