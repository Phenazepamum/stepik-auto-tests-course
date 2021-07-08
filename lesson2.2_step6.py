from selenium import webdriver
import time
import math
from math import log, sin
def calc(x):
  return str(math.log(abs(12*sin(int(x)))))
link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    otvet = browser.find_element_by_id("answer")
    otvet.send_keys(y)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    imrobot = browser.find_element_by_id("robotCheckbox")
    imrobot.click()

    robotrule = browser.find_element_by_id("robotsRule")
    robotrule.click()
    

    button.click()

finally:
    time.sleep(20)
    browser.quit()