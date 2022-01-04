from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link1 = "http://suninjuly.github.io/find_link_text"
try:
    browser=webdriver.Chrome()
    browser.get(link1)
    #link = "str(math.ceil(math.pow(math.pi, math.e)*10000))"
    link=browser.find_element(By.PARTIAL_LINK_TEXT,str(math.ceil(math.pow(math.pi, math.e)*10000)))
    #link=browser.find_element(By.PARTIAL_LINK_TEXT,"Math")
    link.click()
    fild1 = browser.find_element(By.CSS_SELECTOR, "input[name='first_name']")
    fild1.send_keys("Ivan")
    fild2 = browser.find_element(By.CSS_SELECTOR,"form[action='#'] div:nth-child(2) .form-control")
    fild2.send_keys("Petrov")
    #если class = "form-control city"(составной),то перечисляем через точку
    fild3 = browser.find_element(By.CSS_SELECTOR,".form-control.city")
    fild3.send_keys("Smolensk")
    fild4=browser.find_element(By.CSS_SELECTOR,"#country")
    fild4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR,".btn.btn-default")
    button.click()
    time.sleep(15)
finally:
    browser.quit()