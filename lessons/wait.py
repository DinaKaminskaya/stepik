import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from math import sin

def calc(x):
    return math.log(abs(12*sin(x)))

try:
    browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element(By.ID,"book").click()

    num = int(browser.find_element(By.ID,"input_value").text)
    result = calc(num)
    field = browser.find_element(By.ID,"answer").send_keys(result)

    button2 = browser.find_element(By.ID,"solve")
    button_check = button2.get_attribute("disabled")
    assert button_check is None, "Button is disabled"
    button2.click()
    alert = browser.switch_to.alert

    print(alert.text.split(': ')[-1])
    time.sleep(10)
finally:
    browser.quit()




