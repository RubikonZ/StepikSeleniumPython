import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/math.html')

    nmbr = int(browser.find_element_by_id('input_value').text)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(nmbr))

    browser.find_element_by_css_selector('[for=robotCheckbox]').click()    
    browser.find_element_by_css_selector('[for=robotsRule]').click()

    browser.find_element_by_tag_name('button').click()

    time.sleep(5)