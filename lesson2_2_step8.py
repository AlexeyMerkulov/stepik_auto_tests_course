from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'sample.txt')
try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    list = [".form-group [name='firstname']", ".form-group [name='lastname']", ".form-group [name='email']"]
    for x in list:
        el = browser.find_element(By.CSS_SELECTOR, x)
        el.send_keys("Some text")
    download = browser.find_element(By.ID, 'file')
    download.send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    button.click()
finally:
    time.sleep(10)
    browser.quit()