from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select
import time
import math

def sum(x, y):
    return str(x + y)

url = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(url)
    #можно кликнуть на список(если он скрыт),затем кликнуть на нужную строку
    #menu = browser.find_element(By.CSS_SELECTOR,"select#dropdown").click()
    #find_row = browser.find_element(By.CSS_SELECTOR,"select option:nth-child(3)")
    #print(find_row.text)
    #find_row.click()

    #можно используя select
    #menu = Select(browser.find_element(By.CSS_SELECTOR,"select#dropdown"))
    #menu.select_by_value("2")
    #menu.select_by_index(1) #индекс без ковычек
    #menu.select_by_visible_text("91")

    num1 = int(browser.find_element(By.ID,"num1").text)
    print(num1)
    num2 = int(browser.find_element(By.ID,"num2").text)
    print(num2)
    result = sum(num1, num2) 
    print(result)
    menu = Select (browser.find_element(By.CSS_SELECTOR,"#dropdown"))
    menu.select_by_visible_text(result)
    button = browser.find_element(By.CLASS_NAME,"btn").click()
    time.sleep(10)
finally:
    browser.quit()    