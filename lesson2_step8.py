import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name_field = browser.find_element(By.NAME, "firstname")
    name_field.send_keys("Mariia")
    surname_field = browser.find_element(By.NAME, "lastname")
    surname_field.send_keys("Zvereva")
    email_field = browser.find_element(By.NAME, "email")
    email_field.send_keys("test@test.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    attach_button = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    attach_button.send_keys(file_path)
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    #чтобы руками не создавать файл
    #with open("test.txt", "w") as file:
    #    content = file.write("automationbypython")  # create test.txt file

finally:
    time.sleep(10)
    browser.quit()

#current_dir = os.path.abspath(os.path.dirname(__file__))
#file_path = os.path.join(current_dir, 'file.txt')

#print(os.path.abspath(__file__))
#print(os.path.abspath(os.path.dirname(__file__)))