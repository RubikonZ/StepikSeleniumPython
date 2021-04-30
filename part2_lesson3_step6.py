from selenium import webdriver
import math, time

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    browser.find_element_by_tag_name('button').click()

    browser.switch_to.window(browser.window_handles[1])

    nmb = browser.find_element_by_id('input_value').text
    val = math.log(abs(12*math.sin(int(nmb))))

    browser.find_element_by_id('answer').send_keys(str(val))
    browser.find_element_by_tag_name('button').click()

    time.sleep(5)