import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/find_xpath_form')

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ruben")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Zurabyan")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Moscow")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")

    btn = browser.find_element_by_xpath("//button[text()='Submit']")
    btn.click()

    time.sleep(10)