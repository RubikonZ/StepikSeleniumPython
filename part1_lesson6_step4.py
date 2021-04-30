import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/find_link_text')
    link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ruben")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Zurabyan")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Moscow")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    time.sleep(5)