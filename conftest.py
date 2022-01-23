import pytest
import selenium
from selenium import webdriver
from locators import AdminPanel
import pickle


def pytest_addoption(parser):
    parser.addoption('--url',action='store', default='http://localhost/')
    parser.addoption('--path',action='store', default=r'C:\Webdrivers')
    parser.addoption('--br',action='store', default='chrome')

@pytest.fixture
def browser(request):
    url = request.config.getoption('--url')
    path = request.config.getoption('--path')
    if request.config.getoption('--br') == 'chrome':
        driver = webdriver.Chrome(executable_path=path + r'\chromedriver.exe')
    elif request.config.getoption('--br') == 'firefox':
        driver = webdriver.Chrome(executable_path=path + r"\geckodriver.exe")
    driver.maximize_window()
    driver.get(url)
    request.addfinalizer(driver.close)
    return driver


@pytest.fixture
def browser_admin(request,browser):
    browser.get(request.config.getoption('--url') + '/admin/')
    return browser

@pytest.fixture
def browser_admin_inside(browser_admin):
    name = browser_admin.find_element_by_name('username')
    name.send_keys(AdminPanel.Enter_Admin.LOGIN)
    password = browser_admin.find_element_by_name('password')
    password.send_keys(AdminPanel.Enter_Admin.PASSWORD)
    browser_admin.find_element_by_class_name('btn-primary').click()
    return browser_admin


