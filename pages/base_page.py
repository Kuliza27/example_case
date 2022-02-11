""" Module for initializing the web driver Chrome, basic functions and actions on the web page """
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.url = "https://yandex.ru/"
        self.driver.implicitly_wait(timeout)

    def open_page(self):
        """ Opens a web page """
        return self.driver.get(self.url)

    def find_element(self, method, selector):
        """ Looking for one element """
        return self.driver.find_element(method, selector)

    def find_elements(self, method, selector):
        """ Looking for a list of elements """
        return self.driver.find_elements(method, selector)

    def get_attr(self, method, selector, attribute):
        """ Gets the attribute of the element """
        element = self.find_element(method, selector)
        return element.get_attribute(attribute)

    def current_url(self):
        """ Returns current page body """
        return self.driver.current_url

    def switch_to_window(self, index):
        """ Switches to another window by index """
        new_window = self.driver.window_handles[index]
        return self.driver.switch_to.window(new_window)

    def push_enter(self, method, selector):
        """ Presses the enter key """
        enter = self.find_element(method, selector)
        enter.send_keys(Keys.ENTER)
        return enter

    def text_input_in_search_field(self, method, selector, text):
        """ Enters text into the search bar """
        search_field = self.find_element(method, selector)
        search_field.send_keys(text)
        return search_field
