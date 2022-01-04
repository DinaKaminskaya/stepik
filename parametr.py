from types import BuiltinFunctionType
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import pytest

#url = "https://stepik.org/lesson/236895/step/1"

#перенесли фикстуру в conftest + добавили запуск в нескольких браузерах
#@pytest.fixture
#def browser():
#    print("open browser")
#    browser = webdriver.Chrome()
#    yield browser
#    print("close browser")
#    browser.quit()

list_for_result = ''
@pytest.mark.parametrize('url',["236898","236899","236903","236904","236905"])
class Test_result():
    
    def test_1(self,browser,url):
        global list_for_result
        browser.get(f"https://stepik.org/lesson/{url}/step/1")
        browser.implicitly_wait(10)
        
        answer = math.log(int(time.time() + 4.8))
        field = browser.find_element(By.CSS_SELECTOR,"div[data-state='no_submission']>textarea").send_keys(f"{answer}")
        button  = browser.find_element(By.CSS_SELECTOR,"button.submit-submission").click()
        act_result = browser.find_element(By.CSS_SELECTOR,"pre.smart-hints__hint").text
        print(act_result)
        if act_result != "Correct!":
            list_for_result = list_for_result + act_result
            print(list_for_result)
        assert act_result == "Correct!", "Wrong answer"
#print(list_for_result)
        
        
