from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("div:nth-child(1) input")
    input1.send_keys("Ilon")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Musk")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smoke")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Mars")
    button = browser.find_element(By.XPATH, '//button[text() ="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла