import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.locators import BasketLocators
import time


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    time.sleep(2)
    page.add_to_basket()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(2)
    book_name = browser.find_element(*BasketLocators.BOOK_TITLE).text
    book_price = browser.find_element(*BasketLocators.BOOK_PRICE).text

    basket_button = browser.find_element(*BasketLocators.BASKET_BUTTON)
    basket_button.click()
    time.sleep(2)

    full_price = browser.find_element(*BasketLocators.FULL_PRICE).text
    book_basket_name = browser.find_element(*BasketLocators.BASKET_BOOK_TITLE).text

    assert book_name == book_basket_name and book_price == full_price, "Something is wrong"
