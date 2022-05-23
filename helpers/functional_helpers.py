from helpers import credentials


def assert_element_text(self, driver, xpath, expected_text):
    driver.get(credentials.url)
    element = driver.find_element_by_xpath(xpath)
    element_text = element.text
    self.assertEqual(expected_text, element_text,
                     f'Expected text differ from actual on page: {driver.current_url}')

