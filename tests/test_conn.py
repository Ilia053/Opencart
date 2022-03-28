from locators import AdminPanel
import pytest_html
import allure

@allure.feature('Autorif')
@allure.story('right way')
@allure.severity(allure.severity_level.BLOCKER)
def test_connection(browser):
    browser.find_element_by_id('logo')

def test_conn_admin_enter(browser_admin):
    name = browser_admin.find_element_by_name('username')
    name.send_keys(AdminPanel.Enter_Admin.LOGIN['id'])
    password = browser_admin.find_element_by_name('password')
    password.send_keys(AdminPanel.Enter_Admin.PASSWORD)
    browser_admin.find_element_by_class_name('btn-primary').click()


def test_conn_admin_enter(browser_with_log):
    name = browser_with_log.find_element_by_name('username')
    name.send_keys(AdminPanel.Enter_Admin.LOGIN['id'])
    password = browser_with_log.find_element_by_name('password')
    password.send_keys(AdminPanel.Enter_Admin.PASSWORD)
    browser_with_log.find_element_by_class_name('btn-primary').click()

