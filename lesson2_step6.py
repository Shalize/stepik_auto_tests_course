from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    _ = input1.location_once_scrolled_into_view

    input2 = browser.find_element(By.ID, "robotCheckbox").click()
    input3 = browser.find_element(By.ID, "robotsRule").click()
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    print(browser.switch_to.alert.text.split()[-1])

finally:
    time.sleep(10)
    browser.quit()