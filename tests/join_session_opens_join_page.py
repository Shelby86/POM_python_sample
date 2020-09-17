import unittest

from selenium import webdriver

from pages.login_page import LoginPage
from pages.main_page import MainPage
from tests import CHROME_DRIVER


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path=CHROME_DRIVER)
        self.login_page = LoginPage(self.browser)
        self.login_page.go_to_page()
        self.main_page = MainPage(self.browser)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_open_join_session(self):
        self.login_page.login()
        self.main_page.join_session()
        url = self.browser.current_url

        self.assertEqual(url,"https://app.getmetastream.com/join")


if __name__ == '__main__':
    unittest.main()
