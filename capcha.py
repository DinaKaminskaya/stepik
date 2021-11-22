from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))

url="http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(url)
    x_element=browser.find_element(By.CSS_SELECTOR,"#input_value")
    #print(x_element)
    x = x_element.text
    print(x)
    #y = math.log(abs(12*math.sin(int(x))))
    result = calc(x) 
    print(result)
    field = browser.find_element(By.ID,"answer").send_keys(result)
    time.sleep(3)
    box = browser.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
    radio = browser.find_element(By.CSS_SELECTOR,"input#robotsRule").click()
    button = browser.find_element(By.CLASS_NAME,"btn.btn-default").click()
    time.sleep(10)
finally:  
    browser.quit()
