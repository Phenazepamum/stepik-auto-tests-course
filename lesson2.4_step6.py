from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")

try:
    browser.implicitly_wait(5)
    button = browser.find_element_by_id("button")
    button.click()

finally:
    time.sleep(15)
    browser.quit()