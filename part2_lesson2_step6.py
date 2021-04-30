from selenium import webdriver
import math, time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    val = int(browser.find_element_by_id('input_value').text)
    browser.execute_script("window.scrollBy(0, 100);")
    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(val))    
    
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    button = browser.find_element_by_tag_name("button")
    button.click()

    time.sleep(5)

