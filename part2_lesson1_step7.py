import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/get_attribute.html')

    nmbr = int(browser.find_element_by_id('treasure').get_attribute('valuex'))

    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(nmbr))

    browser.find_element_by_id('robotCheckbox').click()    
    browser.find_element_by_id('robotsRule').click()

    browser.find_element_by_tag_name('button').click()

    time.sleep(5)