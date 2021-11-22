from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url="http://suninjuly.github.io/registration2.html"
try:
    browser=webdriver.Chrome()
    browser.get(url)
    #fields=browser.find_elements(By.CSS_SELECTOR,":required")
    #print(len(fields))
    #for el in fields:
    #    el.send_keys("aaa")
    field1=browser.find_element(By.CSS_SELECTOR,".first:required").send_keys("aaa")
    field2=browser.find_element(By.CSS_SELECTOR,".second:required").send_keys("aaa")
    field3=browser.find_element(By.CSS_SELECTOR,".third:required").send_keys("aaa")
    button=browser.find_element(By.CLASS_NAME,"btn").click()
    time.sleep(7)
    #находим элемент с приветствием
    welcome_text=browser.find_element(By.TAG_NAME,"h1")
    #теперь из всего элемента берем только текст для сравнения
    text_res=welcome_text.text
    print(text_res)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    text_exp="Congratulations! You have successfully registered!"
    assert text_exp==text_res
    time.sleep(7)
finally:
    time.sleep(10)
    browser.quit()
    