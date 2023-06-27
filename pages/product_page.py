from .base_page import BasePage
from .locators import AddToBasketLocators as ATBL


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ATBL.ADD_BOOK_TO_BASKET)
        basket_button.click()


