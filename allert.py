from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from math import sin

def calc(x):
    return math.log(abs(12*sin(x)))

url = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
try:
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR,".btn").click()

    alert = browser.switch_to.alert #переключаемся на алерт
    alert.accept() # принять алерт
    #alert.dismiss() #отмена алерт
    #alert.send_keys("ответ") #если алерт с полем для ввода
    number = int(browser.find_element(By.ID,"input_value").text)
    print(number)

    result = calc(number)
    print(result)

    field = browser.find_element(By.ID,"answer").send_keys(result)
    button = browser.find_element(By.CLASS_NAME,"btn").click()

    alert_res = browser.switch_to.alert
    print(alert_res.text)
    time.sleep(5)

    alert_res.accept()
finally:
    browser.quit()
