""" Module for locator class and asserts class """
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class YandexLocators:

    YANDEX_SEARCH_LOCATOR = (By.CSS_SELECTOR, 'input#text')
    SAERCH_SUGGEST_LOCATOR = (By.CSS_SELECTOR, '.mini-suggest__popup.mini-suggest__popup_svg_yes')
    SEARCH_RESULTS_LOCATOR = (By.CSS_SELECTOR, 'ul#search-result li')
    HOME_PAGE_IMAGES_LOCATOR = (By.CSS_SELECTOR, 'ul.services-new__list li:nth-child(3) a')
    FIRST_IMAGE_CATEGORY_LOCATOR = (By.CSS_SELECTOR, 'div.PopularRequestList .PopularRequestList-Item')
    TEXT_IN_SEARCH_LOCATOR = (By.CSS_SELECTOR, 'div.Root')
    FIRST_IMAGE_LOKATOR = (By.CSS_SELECTOR, 'div.serp-list :nth-child(1) img')
    SLIDE_SHOW_LOKATOR = (By.CSS_SELECTOR, 'div.MediaViewer.MediaViewer_theme_fiji.ImagesViewer-Container>div')
    BUTTON_FORWARD_LOCATOR = (By.CSS_SELECTOR, 'div.CircleButton.CircleButton_type_next')
    BUTTON_BACK_LOCATOR = (By.CSS_SELECTOR, 'div.CircleButton.CircleButton_type_prev')
    NAME_IMAGE_LOCATOR = (By.CSS_SELECTOR, 'div.MMOrganicSnippet a.Link')


class Assertions(BasePage):

    def is_element_present_or_visible(self, method, selector):
        """ Checks for the presence of an element on a web page """
        element = self.find_element(method, selector)
        assert element.is_displayed(), f'Element with locator {method, selector} is not found on a page'

    def link_in_results(self, link):
        """ Checks for links in search results """
        res = self.find_elements(*YandexLocators.SEARCH_RESULTS_LOCATOR)
        list_bool = []
        for i in range(5):
            list_bool.append('tensor.ru' in res[i].text)
        assert all(list_bool), f'Link "{link}" is not found in 5 first search results'

    def is_link_on_page(self, link):
        """ Checks for a link on a page """
        element = self.get_attr(*YandexLocators.FIRST_IMAGE_CATEGORY_LOCATOR, 'href')
        assert link in element, f'Link "{link}" is not on page'

    def is_current_link(self, link):
        """ Checks if the link matches the actual link """
        assert link in self.current_url(), f'Link "{link}" is not current'

    def is_selected_image(self, name_category):
        """ Checks if the first category matches the selected category of images """
        text = self.get_attr(*YandexLocators.TEXT_IN_SEARCH_LOCATOR, 'data-state')
        assert name_category in text, 'The text in the search bar does not match the selected category'

    def is_different_image(self, method, selector, first_name):
        """ Checks if two image names do not match """
        second_name = self.find_element(method, selector).text
        assert first_name != second_name, f'Image "{first_name}" has not change'

    def is_same_image(self, method, selector, first_name):
        """ Checks that the picture is the same """
        second_name = self.find_element(method, selector).text
        assert first_name == second_name, 'After pressing the back button, the picture does not match the previous one'
