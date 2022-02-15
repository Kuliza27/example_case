""" Yandex.ru tests module """
from pages.main_page import Assertions, YandexLocators
import pytest


class TestCase1:

    def test_search_present(self, driver):
        """ Make sure the Yandex search field on the page """
        page = Assertions(driver)
        page.open_page()
        page.is_element_present_or_visible(*YandexLocators.YANDEX_SEARCH_LOCATOR)

    def test_suggest_present(self, driver):
        """ Make sure the suggest field on the page """
        page = Assertions(driver)
        page.open_page()
        page.text_input_in_search_field(*YandexLocators.YANDEX_SEARCH_LOCATOR, 'wikipedia')
        page.is_element_present_or_visible(*YandexLocators.SAERCH_SUGGEST_LOCATOR)

    def test_find_links_in_results(self, driver):
        """ Make sure the link to Tensor.ru is in the first five search results """
        page = Assertions(driver)
        page.open_page()
        page.text_input_in_search_field(*YandexLocators.YANDEX_SEARCH_LOCATOR, 'wikipedia')
        page.push_enter(*YandexLocators.YANDEX_SEARCH_LOCATOR)
        page.link_in_results('wikipedia.org')
        
    def test_find_links_in_html_attr_results(self, driver):
        """ Make sure the link to Tensor.ru is in the first five href attribute of search results """
        page = Assertions(driver)
        page.open_page()
        page.text_input_in_search_field(*YandexLocators.YANDEX_SEARCH_LOCATOR, 'wikipedia')
        page.push_enter(*YandexLocators.YANDEX_SEARCH_LOCATOR)
        page.href_in_results('wikipedia.org')
        
        
class TestCase2:
    def test_images_present(self, driver):
        """ Make sure the link to the images section on the main page of Yandex """
        page = Assertions(driver)
        page.open_page()
        page.is_link_on_page('yandex.ru/images')

    def test_current_url(self, driver):
        """ Make sure switched to the page with pictures """
        page = Assertions(driver)
        page.open_page()
        page.find_element(*YandexLocators.HOME_PAGE_IMAGES_LOCATOR).click()
        page.switch_to_window(1)
        page.is_current_link('https://yandex.ru/images/')

    def test_correct_text_in_search(self, driver):
        """ Make sure the text in the search bar matches the name of the selected category of images """
        page = Assertions(driver)
        page.open_page()
        page.find_element(*YandexLocators.HOME_PAGE_IMAGES_LOCATOR).click()
        page.switch_to_window(1)
        name_category = page.get_attr(*YandexLocators.FIRST_IMAGE_CATEGORY_LOCATOR, 'data-grid-text')
        page.find_element(*YandexLocators.FIRST_IMAGE_CATEGORY_LOCATOR).click()
        page.is_selected_image(name_category)

    def test_open_image(self, driver):
        """ Make sure the picture is open """
        page = Assertions(driver)
        page.open_page()
        page.find_element(*YandexLocators.HOME_PAGE_IMAGES_LOCATOR).click()
        page.switch_to_window(1)
        page.find_element(*YandexLocators.FIRST_IMAGE_CATEGORY_LOCATOR).click()
        page.find_element(*YandexLocators.FIRST_IMAGE_LOKATOR).click()
        page.is_element_present_or_visible(*YandexLocators.SLIDE_SHOW_LOKATOR)

    def test_open_another_image(self, driver):
        """ Make sure when you press the forward button, another picture opens """
        page = Assertions(driver)
        page.open_page()
        page.find_element(*YandexLocators.HOME_PAGE_IMAGES_LOCATOR).click()
        page.switch_to_window(1)
        page.find_element(*YandexLocators.FIRST_IMAGE_CATEGORY_LOCATOR).click()
        page.find_element(*YandexLocators.FIRST_IMAGE_LOKATOR).click()
        first_image_name = page.find_element(*YandexLocators.NAME_IMAGE_LOCATOR).text
        page.find_element(*YandexLocators.BUTTON_FORWARD_LOCATOR).click()
        page.is_different_image(*YandexLocators.NAME_IMAGE_LOCATOR, first_image_name)

    def test_back_to_same_image(self, driver):
        """ Make sure when you press the back button, the previous image opens """
        page = Assertions(driver)
        page.open_page()
        page.find_element(*YandexLocators.HOME_PAGE_IMAGES_LOCATOR).click()
        page.switch_to_window(1)
        page.find_element(*YandexLocators.FIRST_IMAGE_CATEGORY_LOCATOR).click()
        page.find_element(*YandexLocators.FIRST_IMAGE_LOKATOR).click()
        first_image_name = page.find_element(*YandexLocators.NAME_IMAGE_LOCATOR).text
        page.find_element(*YandexLocators.BUTTON_FORWARD_LOCATOR).click()
        page.find_element(*YandexLocators.BUTTON_BACK_LOCATOR).click()
        page.is_same_image(*YandexLocators.NAME_IMAGE_LOCATOR, first_image_name)


if __name__ == '__main__':
    pytest.main()
