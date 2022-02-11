""" Module for Pytest fixtures """
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver
