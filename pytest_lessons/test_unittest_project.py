import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class UnitTesting(unittest.TestCase):
    def test_success(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.second").send_keys("Ivanov")
        browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.third").send_keys("@@@")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        expected = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected, f"Should be {expected} but was {welcome_text}")
        browser.quit()

    def test_fail(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.second").send_keys("Ivanov")
        browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.third").send_keys("@@@")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        expected = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected, f"Should be {expected} but was {welcome_text}")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
