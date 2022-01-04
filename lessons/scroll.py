#просколлить страницу пока элемент не станет видимым для клика
#button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#button.click()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from math import sin

def calc(value):
    return math.log(abs(12*sin(value)))

url="http://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(url)
    x_element=int(browser.find_element(By.CSS_SELECTOR,"#input_value").text)
    print(x_element)

    result = calc(x_element) 
    print(result)
    field = browser.find_element(By.ID,"answer").send_keys(result)
    box = browser.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
    #проскролим чтобы избавиться от футера
    browser.execute_script("window.scrollBy(0, 100);")

    radio = browser.find_element(By.CSS_SELECTOR,"#robotsRule").click()
    button = browser.find_element(By.CSS_SELECTOR,".btn")
    button.click()
    time.sleep(10)
finally:  
    browser.quit()
