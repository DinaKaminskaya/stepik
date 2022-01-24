from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class Test_for_language():

    def test_find_button(self,browser):
        browser.get(url)
        time.sleep(5)

        #button = browser.find_elements_by_css_selector("form > .btn-lg")
        button = browser.find_elements(By.CSS_SELECTOR,"form > .btn-lg")
        assert button, "!!!НЕ НАШЕЛ!!!"

    #     x = 0
    #try:
    #    browser.find_element_by_css_selector('button[class*="btn-add-to-basket"]')
    #    x = 1
    #except Exception:
    #    pass
    #finally:
    #    assert x == 1, 'Элемент не найден'
        

        




