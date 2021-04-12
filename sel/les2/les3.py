from selenium import webdriver
import time
import os


try:
    brow = webdriver.Chrome()
    path = 'http://suninjuly.github.io/file_input.html'
    brow.get(path)
    inputs = brow.find_elements_by_tag_name('input')
    for filed in inputs[:3]:
        filed.send_keys('qwerty')
    dirname = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(dirname, 'some.txt')
    brow.find_element_by_id('file').send_keys(file)
    brow.find_element_by_class_name('btn-primary').click()
finally:
    time.sleep(10)
    brow.quit()
