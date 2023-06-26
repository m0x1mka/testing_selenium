import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_guest_can_go_to_login_page(language):
    browser = webdriver.Chrome()
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sllep(30)
    button_to_add_to_basket = browser.find_element(By.CSS_SELECTOR,
                                                   "article form button[type='submit']")
    assert button_to_add_to_basket is not None, "Here is no button!!!"
