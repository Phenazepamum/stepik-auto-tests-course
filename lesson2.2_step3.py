from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id('num2').text
    sum = str(int(x) + int(y))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(sum)

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()