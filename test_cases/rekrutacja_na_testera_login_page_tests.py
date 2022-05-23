import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from helpers import credentials


class RekrutacjaNaTesteraLoginPageTests(unittest.TestCase):

    def setUp(self):
        self.base_url = credentials.url
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('start-maximized')
        self.driver = webdriver.Chrome(executable_path=r"./webdriver/chromedriver.exe", options=chrome_options)
        self.user_login = credentials.user_login
        self.user_pass = credentials.user_pass
        self.user_incorrect_login = 'user'
        self.user_incorrect_pass = 'qwerty'
        self.login_url = ("http://" + self.user_login + ":" + self.user_pass + "@" + self.base_url)

    def tearDown(self):
        self.driver.quit()

    def test_correct_login(self):
        driver = self.driver
        header_xpath = '//h1[@class="title is-1"]'
        expected_text = 'Rekrutacja na testera'
        driver.get(self.login_url)
        self.assert_element_text(driver, header_xpath, expected_text)
        time.sleep(2)

    def assert_element_text(self, driver, xpath, expected_text):
        driver.get("http://tester.tme3c.com/")
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text,
                         f'Expected text differ from actual on page: {driver.current_url}')

