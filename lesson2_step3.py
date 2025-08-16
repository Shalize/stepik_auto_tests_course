from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x, y):
        return str(int(x) + int(y))

    first_number = browser.find_element(By.ID, "num1")
    x = first_number.text
    second_number = browser.find_element(By.ID, "num2")
    y = second_number.text
    sum = calc(x, y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()