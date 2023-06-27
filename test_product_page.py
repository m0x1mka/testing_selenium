import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(2)
    page.add_to_basket()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(2)
