from selenium import webdriver
import math, time

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/alert_accept.html')

    browser.find_element_by_tag_name('button').click()
    browser.switch_to.alert.accept()

    nmb = browser.find_element_by_id('input_value').text
    val = math.log(abs(12*math.sin(int(nmb))))

    browser.find_element_by_id('answer').send_keys(str(val))

    browser.find_element_by_css_selector('button.btn').click()

    time.sleep(5)