import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/huge_form.html')
    fields = browser.find_elements_by_tag_name('input')
    for field in fields:
        field.send_keys('Privit')

    btn = browser.find_element_by_tag_name('button')
    btn.click()
    time.sleep(10)