from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    browser=webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    #find_elements-берет все эленемны по заданному критерию,
    #find_element-находит только первый.
    fild=browser.find_elements(By.TAG_NAME,"input")
    #команда assert len(fild)-проверит кол-во найденных элементов
    assert len(fild)==100
    print(len(fild)) #посчитать
    for el in fild:
        el.send_keys("мой ответ")
    button=browser.find_element(By.TAG_NAME,"button")
    button.click()
    time.sleep(15)
finally:
    browser.quit()
