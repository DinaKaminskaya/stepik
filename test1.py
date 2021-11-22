from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link="http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    #while(True):
    #    pass
    #time.sleep(15)
    fild1 = browser.find_element(By.CSS_SELECTOR, "input[name='first_name']")
    fild1.send_keys("Ivan")
    fild2 = browser.find_element(By.CSS_SELECTOR,"form[action='#'] div:nth-child(2) .form-control")
    fild2.send_keys("Petrov")
    #если class = "form-control city"(составной),то перечисляем через точку
    fild3 = browser.find_element(By.CSS_SELECTOR,".form-control.city")
    fild3.send_keys("Smolensk")
    fild4=browser.find_element(By.CSS_SELECTOR,"#country")
    fild4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR,"#submit_button")
    button.click()
    time.sleep(15)
    #browser.quit()
finally:
    browser.quit()
