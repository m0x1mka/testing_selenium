import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    button_to_add_to_basket = browser.find_element(By.CSS_SELECTOR,
                                                   "article form button[type='submit']")
    assert button_to_add_to_basket is not None, "Your selectors are wrong"
