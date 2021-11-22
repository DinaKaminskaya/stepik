from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
url="http://suninjuly.github.io/find_xpath_form "
try:
    browser=webdriver.Chrome()
    browser.get(url)
    fild1=browser.find_element(By.XPATH,"//input[@name='first_name']").send_keys("fff")
    fild2=browser.find_element(By.XPATH,"//form[@action='#']/div[2]/input").send_keys("fff")
    fild2=browser.find_element(By.XPATH,"//form[@action='#']/div[3]/input").send_keys("fff")
    fild2=browser.find_element(By.XPATH,"//form[@action='#']/div[4]/input").send_keys("fff")
    button=browser.find_element(By.XPATH,"//button[text()='Submit']").click()
    time.sleep(10)
finally:
    browser.quit()
    