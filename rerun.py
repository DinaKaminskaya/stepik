#когда надо запустить один и тот же тест несколько раз из-за предсказуемого падения pip install pytest-rerunfailures
# запуск pytest -v --tb=line --reruns 1 имя файла
import pytest
link = "http://selenium1py.pythonanywhere.com/"

def test_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

@pytest.mark.flaky(reruns = 1) # можно добавить как маркировку-тогда не передавать в параметрах запуска + доб в ini
def test_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")