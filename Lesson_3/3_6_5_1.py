import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

links = ["https://stepik.org/lesson/236895/step/1",
             "https://stepik.org/lesson/236896/step/1",
             "https://stepik.org/lesson/236897/step/1",
             "https://stepik.org/lesson/236898/step/1",
             "https://stepik.org/lesson/236899/step/1",
             "https://stepik.org/lesson/236903/step/1",
             "https://stepik.org/lesson/236904/step/1",
             "https://stepik.org/lesson/236905/step/1"]

browser = webdriver.Chrome()
for link in links:
    try:
        browser.get(link)
        time.sleep(2)
        log_in_button = browser.find_element(By.ID, "ember33")
        log_in_button.click()

        email_field = browser.find_element(By.ID, "id_login_email")
        email_field.send_keys("reebok81@mail.ru")

        password_field = browser.find_element(By.ID, "id_login_password")
        password_field.send_keys('17108481kmld')
        button_to_log_in = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
        button_to_log_in.click()

        time.sleep(2)
        button = browser.find_element(By.CLASS_NAME, "again-btn.white")
        button.click()
        browser.quit()
    except:
        print("This link is OK")
