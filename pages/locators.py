from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "registration_link")


class AddToBasketLocators:
    ADD_BOOK_TO_BASKET = (By.CSS_SELECTOR, 'form[id="add_to_basket_form"] button[type="submit"]')


class BasketLocators:
    BOOK_TITLE = (By.CSS_SELECTOR, 'div[id="content_inner"] h1')
    BOOK_PRICE = (By.CSS_SELECTOR, 'div[id="content_inner"] p')
    BASKET_BUTTON = (By.CSS_SELECTOR, 'span[class="btn-group"] a')
    FULL_PRICE = (By.CSS_SELECTOR, 'p[class="price_color align-right"]')
    BASKET_BOOK_TITLE = (By.CSS_SELECTOR, 'div[class="col-sm-4"] a')
