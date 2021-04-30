from selenium import webdriver
import math, time, os

with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    browser.find_element_by_css_selector('[name=email]').send_keys('q@mail.com')
    browser.find_element_by_css_selector('[name=firstname]').send_keys('R')
    browser.find_element_by_css_selector('[name=lastname]').send_keys('Z')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'topkek.txt')           # добавляем к этому пути имя файла 
    browser.find_element_by_id("file").send_keys(file_path)

    browser.find_element_by_tag_name('button').click()

    time.sleep(5)


