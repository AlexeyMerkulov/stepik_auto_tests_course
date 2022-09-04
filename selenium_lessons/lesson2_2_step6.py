from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, 'input_value').text)
    rsl = math.log(abs(12 * math.sin(x)))
    resp = browser.find_element(By.ID, 'answer')
    resp.send_keys(rsl)
    button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    button.click()
finally:
    time.sleep(10)
    browser.quit()
