import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/selects1.html')
    val = int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text)
    select = Select(browser.find_element_by_id('dropdown'))

    select.select_by_value(str(val))

    browser.find_element_by_tag_name('button').click()

    time.sleep(5)


