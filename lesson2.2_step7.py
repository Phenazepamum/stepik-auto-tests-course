import time
import os
from selenium import webdriver
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    name = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
    name.send_keys("Ilon")
    lastname = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
    lastname.send_keys("Musk")
    email = browser.find_element_by_css_selector('[placeholder="Enter email"]')
    email.send_keys("Rogozin@sasat.dno")


    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_css_selector("[type='file']")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    time.sleep(20)
    browser.quit()