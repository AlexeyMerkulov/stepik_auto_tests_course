from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, 'btn-primary').click()
    browser.switch_to.alert.accept()
    x = int(browser.find_element(By.ID, 'input_value').text)
    rsl = math.log(abs(12 * math.sin(x)))
    field = browser.find_element(By.ID, 'answer')
    field.send_keys(rsl)
    browser.find_element(By.CLASS_NAME, 'btn-primary').click()
finally:
    time.sleep(8)
    browser.quit()