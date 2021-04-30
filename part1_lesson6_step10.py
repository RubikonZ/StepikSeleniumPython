import math
from selenium import webdriver
import time

with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/registration1.html')
    #browser.get('http://suninjuly.github.io/registration2.html')

    input1 = browser.find_element_by_css_selector(".first_block .first")
    input1.send_keys("R")
    input2 = browser.find_element_by_css_selector(".first_block .second")
    input2.send_keys("Z")
    input3 = browser.find_element_by_css_selector(".first_block .third")
    input3.send_keys("r@z.mail.com")

    btn = browser.find_element_by_css_selector('button.btn')
    btn.click()

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(2)