from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    path = 'http://suninjuly.github.io/selects1.html'
    brow = webdriver.Chrome()
    brow.get(path)
    num1 = brow.find_element_by_id('num1')
    num2 = brow.find_element_by_id('num2')
    sum = int(num1.text) + int(num2.text)
    select = Select(brow.find_element_by_tag_name('select'))
    select.select_by_value(str(sum))
    brow.find_element_by_class_name('btn-default').click()
finally:
    time.sleep(10)
    brow.quit()
