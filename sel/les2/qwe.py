from selenium import webdriver
import time


try:
    back = 'im-page--back-btn'
    brow = webdriver.Chrome()
    brow.implicitly_wait(5)
    path = 'https://vk.com/im?sel=209562471'
    brow.get(path)
    brow.find_element_by_id('email').send_keys()
    brow.find_element_by_id('pass').send_keys()
    brow.find_element_by_id('login_button').click()
    brow.find_element_by_id('l_msg').click()
    while True:
        new = brow.find_elements_by_css_selector('.nim-dialog_unread')
        if new:
            new[0].click()
            brow.find_element_by_css_selector('.im_editable.im-chat-input--text._im_text').send_keys('fet')
            brow.find_element_by_css_selector('.im-send-btn.im-chat-input--send._im_send.im-send-btn_send').click()
            brow.find_element_by_class_name(back).click()
finally:
    time.sleep(300)
    brow.quit()