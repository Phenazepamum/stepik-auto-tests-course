from selenium import webdriver
browser = webdriver.Chrome()
import time
import math
from math import log, sin
def calc(x):
  return str(log(abs(12*sin(int(x)))))
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

try:
    jorneybtn = browser.find_element_by_css_selector(".btn.btn-primary").click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    submitbtn = browser.find_element_by_class_name("btn.btn-primary").click()
finally:
    time.sleep(20)
    browser.quit()