import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from locators import AdminPanel
import pytest
import pickle
import os
from dataclasses import dataclass, asdict
import requests

# def test():
#     dr = webdriver.Chrome(f'C:\WebDrivers\chromedriver.exe')
#     # act = ActionChains(dr)
#
#     dr.get('http://localhost/admin/')
#     name = dr.find_element_by_name('username')
#     name.send_keys(AdminPanel.Enter_Admin.LOGIN)
#     password = dr.find_element_by_name('password')
#     password.send_keys(AdminPanel.Enter_Admin.PASSWORD)
#     dr.find_element_by_class_name('btn-primary').click()
#     cat = dr.find_element_by_class_name('collapsed')
#     cat.click()
#     sleep(2)
#     lis_pro = dr.find_element_by_id('collapse1').find_elements_by_tag_name('li')
#     lis_pro[1].click()
#     sleep(2)
# # # dr.find_element_by_css_selector('#form-product > div > table > tbody > tr:nth-child(5) > td:nth-child(1) > input[type=checkbox]').click()
# # # dr.find_element_by_class_name('btn-danger').click()
# # # Alert(dr).accept()
#     with pytest.raises(NoSuchElementException):
#         exx = dr.find_element_by_xpath(("//img[@alt='Canon ES 5D']"))
#
# #
#     sleep(5)
#     dr.close()
#     dr.quit()

# dr = webdriver.Chrome(executable_path=f'C:\WebDrivers\chromedriver.exe')

# dr.get('http://localhost/admin/')
# name = dr.find_element_by_name('username')
# name.send_keys(AdminPanel.Enter_Admin.LOGIN)
# password = dr.find_element_by_name('password')
# password.send_keys(AdminPanel.Enter_Admin.PASSWORD)
# dr.find_element_by_class_name('btn-primary').click()
# # pickle.dump(dr.get_cookies(), open('cookies', 'wb'))
# sleep(2)
# logo = dr.find_element_by_css_selector('#header-logo > a > img')
# print(logo.value_of_css_property('color'))
# print('Hello') if logo.value_of_css_property('color') == 'rgba(31, 145, 207, 1)' else print("error")
#
#
# dr.close()

# dr.get('https://marcojakob.github.io/dart-dnd/basic/')
# contain = dr.find_element_by_class_name('container')
# basket = dr.find_element_by_css_selector('body > div > div')
# lis = contain.find_elements_by_class_name('document')
# for i in range(len(lis)):
#     act = ActionChains(dr)
#     act.drag_and_drop(lis[i],basket).perform()
#     sleep(1)
#
# dr.close()
# dr = webdriver.Chrome(f'C:\WebDrivers\chromedriver.exe')
# dr.get('http://localhost/admin/')
# dr.execute_script('window.open()')
# print(dr.window_handles)
# dr.switch_to.window(dr.window_handles[1])
# dr.get('http://ya.ru')
# dr.switch_to.window(dr.window_handles[0])

# dirname = os.path.dirname(__file__)
# name = os.path.join(dirname, '0.txt')


r = requests.get('https://ip-api.com/json/172.28.0.1')
print(r.json())