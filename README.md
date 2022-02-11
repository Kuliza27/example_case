# Introduction
This repository contains a script for automated tests of the Yandex site in Python. It implements a PageObject pattern using libraries Selenium, Pytest
# Files
conftest.py contains Pytest fixtures for initialization the webdriver.

pages/base.py contains PageObject pattern implementation for Python.

pages/main.py contains helper class web elements locators and class allerts.

tests/yandex_test.py contains two sets Web UI tests for Yandex (https://yandex.ru/)
# How To Run Tests
1. Install all requirements:
```
pip3 install -r requirements
```
2. Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)/
3. Run tests:
```
$python3 pytest -r yandex_test.py
```
