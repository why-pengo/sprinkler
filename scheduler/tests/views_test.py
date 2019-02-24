from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_landing_page_title(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('Sprinkler Controller ][', self.browser.title)
