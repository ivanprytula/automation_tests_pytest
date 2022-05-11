"""
driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.

driver.get('https://www.google.com/');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()
"""

from pytest import mark


# @mark.smoke
# @mark.body
class BodyTests:

    # @mark.ui
    def test_can_navigate_to_body_page(self, chrome_browser):
        chrome_browser.get("https://www.motortrend.com/")
        assert True

    # @mark.door
    def test_body_functions_as_expected(self):
        assert True

    @staticmethod
    def test_glass():
        assert True
