import unittest

from helpers import credentials
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as W


class RekrutacjaNaTesteraFrontPageTests(unittest.TestCase):

    def setUp(self):
        self.base_url = credentials.url
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('start-maximized')
        self.driver = webdriver.Chrome(executable_path=r"./webdriver/chromedriver.exe", options=chrome_options)
        self.user_login = credentials.user_login
        self.user_pass = credentials.user_pass
        self.login_url = ("http://" + self.user_login + ":" + self.user_pass + "@" + self.base_url)

    def tearDown(self):
        self.driver.quit()

    def test_zapisz_sie_juz_dzis_header(self):
        expected_text = 'Zapisz sie już dziś'
        header_xpath = '//h1[@class="title is-4"]'
        driver = self.driver
        driver.get("http://" + self.user_login + ":" + self.user_pass + "@" + self.base_url)
        self.assert_element_text(driver, header_xpath, expected_text)

    def test_zapisz_sie_juz_dzis_description(self):
        expected_text = 'Your new job in a cool team is waiting for you!'
        header_xpath = '//div[@class="column right has-text-centered"]/p[@class="description"]'
        driver = self.driver
        driver.get(self.login_url)
        self.assert_element_text(driver, header_xpath, expected_text)

    def test_slogan(self):
        expected_text = 'Odpowiadamy każdemu kandydatowi!'
        header_xpath = '//form[@id="test-form"]/small[@class="slogan"]'
        driver = self.driver
        driver.get(self.login_url)
        self.assert_element_text(driver, header_xpath, expected_text)

    def test_rekrutacja_na_testera_header(self):
        expected_text = 'Rekrutacja na testera'
        header_xpath = '//h1[@class="title is-1"]'
        driver = self.driver
        driver.get(self.login_url)
        self.assert_element_text(driver, header_xpath, expected_text)

    def test_tme_header(self):
        expected_text = 'Transfer Multisort Elektronik'
        header_xpath = '//h1[@class="subtitle colored is-4"]'
        driver = self.driver
        driver.get(self.login_url)
        self.assert_element_text(driver, header_xpath, expected_text)

    def test_tme_paragraph(self):
        expected_text = 'Formularz został stworzony wyłącznie do celów rekrutacji. Nie ma praktycznego zastosowania ' \
                        'poza mozliwością wykazania się dla przyszłych kandydatów. Powodzenia!'
        header_xpath = '//div[@class="column left flip"]/p'
        driver = self.driver
        driver.get(self.login_url)
        self.assert_element_text(driver, header_xpath, expected_text)

    def test_tme_footer(self):
        expected_text = '© Transfer Multisort Elektronik. All Rights Reserved.'
        header_xpath = '//h1[@class="level-item"]'
        driver = self.driver
        driver.get(self.login_url)
        self.assert_element_text(driver, header_xpath, expected_text)

    def test_terms_of_service_is_selected(self):
        driver = self.driver
        driver.get(self.login_url)
        checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']:first-of-type")
        print(f'Checkbox is selected: {checkbox.is_selected()}')

    def test_terms_of_service_select(self):
        driver = self.driver
        driver.get(self.login_url)
        checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']:first-of-type")
        checkbox.click()
        print(f'Checkbox is selected: {checkbox.is_selected()}')

    def test_button_wyslij_is_disabled_when_signin_input_is_empty(self):
        driver = self.driver
        driver.get(self.login_url)
        login_next_button_element = driver.find_element_by_xpath('//button[@class="button is-block is-primary '
                                                                 'is-fullwidth is-medium"]')
        login_next_button_disabled = login_next_button_element.get_property('disabled')
        self.assertEqual(True, login_next_button_disabled,
                         f'Expected state of "Wyślij!" button: True , differ from actual: {login_next_button_disabled}'
                         f', for page url: {driver.current_url}')

    def test_sign_in_using_correct_values(self):
        driver = self.driver
        driver.get(self.login_url)
        country = Select(driver.find_element_by_id('country'))
        country_data = 'Polska'
        country.select_by_visible_text(country_data)
        name = driver.find_element_by_id("name")
        name.clear()
        name_data = 'Jan'
        name.send_keys(name_data)
        password = driver.find_element_by_id('password')
        password.clear()
        password_data = 'qWerty'
        password.send_keys(password_data)
        email = driver.find_element_by_name('email')
        email.clear()
        email_data = 'example@domain.com'
        email.send_keys(email_data)
        checkbox = driver.find_element_by_css_selector("input[type='checkbox']:first-of-type")
        checkbox.click()
        send_button = driver.find_element_by_xpath('//button[@class="button is-block is-primary '
                                                   'is-fullwidth is-medium"]')
        send_button.submit()
        self.assertIn(country_data, driver.find_element_by_xpath('//div[@class="mt-2 md-2 column is-8 is-offset-2"]'
                                                                 '/pre').text, "Comparison Done")
        self.assertIn(name_data, driver.find_element_by_xpath('//div[@class="mt-2 md-2 column is-8 is-offset-2"]'
                                                              '/pre').text, "Comparison Done")
        self.assertIn(password_data, driver.find_element_by_xpath('//div[@class="mt-2 md-2 column is-8 is-offset-2"]'
                                                                  '/pre').text, "Comparison Done")
        self.assertIn(email_data, driver.find_element_by_xpath('//div[@class="mt-2 md-2 column is-8 is-offset-2"]'
                                                               '/pre').text, "Comparison Done")

    def test_sign_in_using_correct_values_and_incorrect_password(self):
        driver = self.driver
        driver.get(self.login_url)
        country = Select(driver.find_element_by_id('country'))
        country_data = 'Polska'
        country.select_by_visible_text(country_data)
        name = driver.find_element_by_id("name")
        name.clear()
        name_data = 'Jan'
        name.send_keys(name_data)
        password = driver.find_element_by_id('password')
        password.clear()
        password_data = '1234'
        password.send_keys(password_data)
        email = driver.find_element_by_name('email')
        email.clear()
        email_data = 'example@domain.com'
        email.send_keys(email_data)
        checkbox = driver.find_element_by_css_selector("input[type='checkbox']:first-of-type")
        checkbox.click()
        send_button = driver.find_element_by_xpath('//button[@class="button is-block is-primary '
                                                   'is-fullwidth is-medium"]')
        send_button.click()
        self.assertIn(password_data, driver.find_element_by_xpath('//div[@class="mt-2 md-2 column is-8 is-offset-2"]'
                                                                  '/pre').text, "Comparison Done")

    def test_sign_in_using_correct_values_and_incorrect_email(self):
        driver = self.driver
        driver.get(self.login_url)
        country = Select(driver.find_element_by_id('country'))
        country_data = 'Polska'
        country.select_by_visible_text(country_data)
        name = driver.find_element_by_id("name")
        name.clear()
        name_data = 'Jan'
        name.send_keys(name_data)
        password = driver.find_element_by_id('password')
        password.clear()
        password_data = 'qWerty'
        password.send_keys(password_data)
        email = driver.find_element_by_name('email')
        email.clear()
        email_data = 'example.com'
        email.send_keys(email_data)
        checkbox = driver.find_element_by_css_selector("input[type='checkbox']:first-of-type")
        checkbox.click()
        send_button = driver.find_element_by_xpath('//button[@class="button is-block is-primary '
                                                   'is-fullwidth is-medium"]')
        send_button.click()
        self.assertIn(f"Email: {email_data}", driver.find_element_by_xpath('//div[@class="mt-2 md-2 column is-8 '
                                                                           'is-offset-2"]''/pre'
                                                                           ).text, "Comparison Done")

    def test_sign_in_using_correct_values_check_country_list_is_clickable(self):
        driver = self.driver
        driver.get(self.login_url)
        country_menu = Select(driver.find_element_by_id('country'))
        country_data = 'Francja'
        country_menu.select_by_visible_text(country_data)
        name = driver.find_element_by_id("name")
        name.clear()
        name_data = 'Jan'
        name.send_keys(name_data)
        password = driver.find_element_by_id('password')
        password.clear()
        password_data = 'qWerty'
        password.send_keys(password_data)
        email = driver.find_element_by_name('email')
        email.clear()

        checkbox = driver.find_element_by_css_selector("input[type='checkbox']:first-of-type")
        checkbox.click()
        send_button = driver.find_element_by_xpath('//button[@class="button is-block is-primary '
                                                   'is-fullwidth is-medium"]')
        send_button.submit()
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element_by_id('country'))
        try:
            actions.click(driver.find_element_by_xpath('//*[@id="country"]'))
        except WebDriverException:
            print(f'Menu is not clickable')

    def test_check_twitter_button(self):
        driver = self.driver
        driver.get(self.login_url)
        expected_link = 'https://twitter.com/tme_eu'
        element = driver.find_element_by_css_selector('a.icon:nth-child(1)')
        element.click()
        self.assertEqual(driver.current_url, expected_link, f'Expected link of Twitter Button, differ from actual: '
                                                            f'{driver.current_url}')

    def test_check_facebook_button(self):
        driver = self.driver
        driver.get(self.login_url)
        expected_link = 'https://pl-pl.facebook.com/TME.eu/'
        element = driver.find_element_by_css_selector('a.icon:nth-child(2)')
        element.click()
        self.assertEqual(driver.current_url, expected_link, f'Expected link of Facebook Button, differ from actual: '
                                                            f'{driver.current_url}')

    def test_check_github_button(self):
        driver = self.driver
        driver.get(self.login_url)
        expected_link = 'https://github.com/tme-dev/TME-API'
        element = driver.find_element_by_css_selector('a.icon:nth-child(4)')
        element.click()
        self.assertEqual(driver.current_url, expected_link, f'Expected link of GitHub Button, differ from actual: '
                                                            f'{driver.current_url}')

    def test_list_contain_exact_number_of_elements(self):
        driver = self.driver
        driver.get(self.login_url)
        expected_number_of_elements = 4
        xpath = '//select[@id="country"]//option'
        elements = driver.find_elements(By.XPATH, xpath)
        number_of_elements = len(elements)
        self.assertEqual(expected_number_of_elements, number_of_elements, 'Elements differ from actual for page '
                                                                          f'{driver.current_url}')

    def test_check_links(self):
        driver = self.driver
        driver.get(self.login_url)
        wait_time_out = 15
        wait = W(driver, wait_time_out)
        links = wait.until(EC.visibility_of_any_elements_located((By.TAG_NAME, "a")))
        print("The total number of links is", len(links))
        for link in links:
            print(link.get_attribute('href'))

    def assert_element_text(self, driver, xpath, expected_text):
        driver.get("http://tester.tme3c.com/")
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text,
                         f'Expected text differ from actual on page: {driver.current_url}')
