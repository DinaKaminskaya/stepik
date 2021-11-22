from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url="http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(5)
    people_radio = browser.find_element(By.ID,"peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked =="true", "People radio is not selected by default"

    radio_robot = browser.find_element(By.CSS_SELECTOR,"#robotsRule")
    check_radio_robot = radio_robot.get_attribute("checked")
    print("value of robots_radio: ",check_radio_robot)
    assert check_radio_robot is None, "Robot radio is selected by default"

    button = browser.find_element(By.CLASS_NAME,"btn.btn-default")
    check_button = button.get_attribute("disabled")
    print("value of button: ",check_button)
    assert check_button is None, "button is disabled"

    time.sleep(10)
    button = browser.find_element(By.CLASS_NAME,"btn.btn-default")
    check_button = button.get_attribute("disabled")
    print("value of button after 10sec: ",check_button)
    assert check_button is not None, "button is not disabled after 10 sec"

finally:  
    browser.quit()
      