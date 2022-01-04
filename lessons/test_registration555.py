from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
#url = "http://suninjuly.github.io/registration1.html"
#url2 = "http://suninjuly.github.io/registration2.html"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser=webdriver.Chrome()
    #browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
#fields=browser.find_elements(By.CSS_SELECTOR,":required")
#for el in fields:
    #    el.send_keys("aaa")
@pytest.mark.parametrize('url',["http://suninjuly.github.io/registration1.html","http://suninjuly.github.io/registration2.html"])    
class Testreg1():
    @pytest.mark.regress # маркируем,если захотим вызвать только регресс
    def test_req_field(self, browser,url):
        print(f"\nstart test1 for {url}")
        browser.get(url)    
        first_name = browser.find_element(By.CSS_SELECTOR,".first_class > .first").get_attribute("required")
        assert first_name == "true", "field 'first_name' is not required"

    @pytest.mark.regress
    def test_req_field2(self,browser,url):
        print(f"\nstart test2 for {url} ")
        browser.get(url)
        last_name = browser.find_element(By.CSS_SELECTOR,".second_class >.second").get_attribute("required")
        assert last_name == "true", "field 'last_name' is not required"
    
    #@pytest.mark.skip #если хотим пропустить тест(заносить в ini не надо)
    def test_reg(self,browser,url):
        print(f"\nstart test3 for {url} ")
        browser.get(url)
        
        field1=browser.find_element(By.CSS_SELECTOR,".first:required").send_keys("aaa")
        field2=browser.find_element(By.CSS_SELECTOR,".second:required").send_keys("aaa")
        field3=browser.find_element(By.CSS_SELECTOR,".third:required").send_keys("aaa")
        button=browser.find_element(By.CLASS_NAME,"btn").click()
        welcome_text=browser.find_element(By.TAG_NAME,"h1")
##теперь из всего элемента берем только текст для сравнения
        text_res=welcome_text.text
#print(text_res)
## с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        text_exp="Congratulations! You have successfully registered!"
        assert text_exp==text_res, "no rigistration failed"