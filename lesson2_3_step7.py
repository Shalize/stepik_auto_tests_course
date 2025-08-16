from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    book_button = browser.find_element(By.ID, "book").click()

    answer_field = browser.find_element(By.ID, "answer")
    _ = answer_field.location_once_scrolled_into_view

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer_field.send_keys(y)

    submit_button = browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(10)
    browser.quit()