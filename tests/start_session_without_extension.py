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

    def test_start_stream_without_extension(self):
        self.login_page.login()
        self.main_page.start_session()

        extension_required_message = self.browser.find_element_by_xpath("//p[contains(text(),'required')]").text
        self.assertIn("extension is required for playback", extension_required_message)



if __name__ == '__main__':
    unittest.main()
