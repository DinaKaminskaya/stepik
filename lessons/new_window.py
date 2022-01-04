#browser.switch_to.window(window_name) переключиться на другую вкладку
#new_window = browser.window_handles[1] 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return math.log(abs(12*sin(x)))
from math import sin
url = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(url)
    field = browser.find_element(By.CLASS_NAME,"trollface.btn").click()
    time.sleep(5)
    #print(browser.window_handles[1])- [1]-второе окно,[0]-первое окно
    new_wind = browser.window_handles[1]
    browser.switch_to.window(new_wind)

    num = int(browser.find_element(By.ID,"input_value").text)
    print(num)
    result = calc(num)
    field2 = browser.find_element(By.ID,"answer").send_keys(result)
    button = browser.find_element(By.CLASS_NAME,"btn").click()
    time.sleep(3)
    alert = browser.switch_to.alert
    print(alert.text.split(': ')[-1])
    alert.accept()

finally:
    browser.quit()