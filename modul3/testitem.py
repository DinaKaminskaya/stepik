from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class Test_for_language():

    def test_find_button(self,browser):
        browser.get(url)
        time.sleep(10)

        button = browser.find_elements_by_css_selector("form > .btn-lg")
        assert button, "!!!НЕ НАШЕЛ!!!"
        




