from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestCssSelectors(unittest.TestCase):
    def test_selectors_one(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        el1 = browser.find_element(By.CSS_SELECTOR, "input.first:required")
        el1.send_keys("a")
        el2 = browser.find_element(By.CSS_SELECTOR, "input.second:required")
        el2.send_keys("a")
        el3 = browser.find_element(By.CSS_SELECTOR, "input.third:required")
        el3.send_keys("a")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        browser.quit()
        self.assertEquals("Congratulations! You have successfully registered!", welcome_text,
                          "Your selectors are wrong!")

    def test_selectors_two(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        el1 = browser.find_element(By.CSS_SELECTOR, "input.first:required")
        el1.send_keys("a")
        el2 = browser.find_element(By.CSS_SELECTOR, "input.second:required")
        el2.send_keys("a")
        el3 = browser.find_element(By.CSS_SELECTOR, "input.third:required")
        el3.send_keys("a")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        browser.quit()
        self.assertEquals("Congratulations! You have successfully registered!", welcome_text,
                          "Your selectors are wrong!")


if __name__ == "__main__":
    unittest.main()
