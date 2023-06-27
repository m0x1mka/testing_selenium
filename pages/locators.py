from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "registration_link")


class AddToBasketLocators:
    ADD_BOOK_TO_BASKET = (By.CSS_SELECTOR, 'form[id="add_to_basket_form"] button[type="submit"]')
