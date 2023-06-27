from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestCssSelectors:
    answer = ""
    links = ["https://stepik.org/lesson/236895/step/1",
             "https://stepik.org/lesson/236896/step/1",
             "https://stepik.org/lesson/236897/step/1",
             "https://stepik.org/lesson/236898/step/1",
             "https://stepik.org/lesson/236899/step/1",
             "https://stepik.org/lesson/236903/step/1",
             "https://stepik.org/lesson/236904/step/1",
             "https://stepik.org/lesson/236905/step/1"]

    @pytest.mark.parametrize("link", links)
    def test_links(self, browser, link):
        browser.get(link)
        time.sleep(4)

        log_in_button = browser.find_element(By.ID, "ember33")
        log_in_button.click()

        email_field = browser.find_element(By.ID, "id_login_email")
        email_field.send_keys("reebok81@mail.ru")

        password_field = browser.find_element(By.ID, "id_login_password")
        password_field.send_keys('17108481kmld')

        button_to_log_in = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
        button_to_log_in.click()
        time.sleep(4)

        answer_field = browser.find_element(By.ID, "ember94")
        answer_field.send_keys(math.log(int(time.time())))

        answer_button = browser.find_element(By.CSS_SELECTOR, "[class='submit-submission']")
        answer_button.click()

        txt_field = browser.find_element(By.CSS_SELECTOR, "[class='smart-hints__hint']").text

        assert txt_field.text == "Correct!", "Your code is wrong"
        if txt_field.text != "Correct!":
            self.answer += txt_field.text
