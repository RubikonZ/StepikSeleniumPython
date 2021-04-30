from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/wait2.html")

    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'verify'))).click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

    time.sleep(2)