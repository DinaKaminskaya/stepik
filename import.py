from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
url="http://suninjuly.github.io/file_input.html"
directory = "C:/Users/dina/env/selenium_env/"
file_name = "1.txt"
file_path = os.path.join(directory, file_name)
try:
    browser=webdriver.Chrome()
    browser.get(url)
    fields=browser.find_elements(By.CSS_SELECTOR,".form-control:required")
    
    for el in fields:
        el.send_keys("aaa")

    import_file = browser.find_element(By.CSS_SELECTOR,"#file").send_keys(file_path)    
    
    button=browser.find_element(By.CLASS_NAME,"btn").click()
    time.sleep(7)
    
finally:
    time.sleep(10)
    browser.quit()
    