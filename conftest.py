import pytest
import selenium
from selenium import webdriver
from locators import AdminPanel
import pickle
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import platform
# import telegram_send

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
    name.send_keys(AdminPanel.Enter_Admin.LOGIN['id'])
    password = browser_admin.find_element_by_name('password')
    password.send_keys(AdminPanel.Enter_Admin.PASSWORD)
    browser_admin.find_element_by_class_name('btn-primary').click()
    return browser_admin

@pytest.fixture
def remote_drive(request):
    wd = webdriver.Remote('http://localhost:4444/wd/hub',desired_capabilities={'browserName':'chrome','version':'','platform':'ANY'})

    # request.addfinalizer(wd.quit())
    return wd

@pytest.fixture
def browser_with_log(request):
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'performance': 'ALL'}
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_experimental_option('w3c',False)
    wd = EventFiringWebDriver(webdriver.Chrome(executable_path=r'C:\Webdrivers\chromedriver.exe',options=options,desired_capabilities=d), Mylistener())
    # request.addfinalizer(wd.close())
    return wd


class Mylistener(AbstractEventListener):

    def before_find(self, by, value, driver):
        print('!!!!!!!!!!!!!!!!!!!')

    def after_find(self, by, value, driver):
        print("11111111111111111111111")

    def on_exception(self, exception, driver):
        print('eeeeeeeeeeeeeee')


@pytest.mark.usefixtures('enviroment_info')
@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request):
    # request.config._metadata.update(
    #     {'foo': 'bar'}
    # )
    pass

@pytest.fixture(scope='session')
def enviroment_info():
    os = platform.platform()
    return os



@pytest.mark.skip
def test_1(browser_with_log):
    browser_with_log.get('http://localhost/admin/')
    time.sleep(2)
    # browser_with_log.save_screenshot('3333.png')
    browser_with_log.find_element_by_class_name('input-group-addon')
    # telegram_send.send(messages=['Done!'])
    print(browser_with_log.log_types)

@pytest.mark.skip
def test_2(remote_drive):
    remote_drive.get('https://mne.tools/stable/auto_tutorials/intro/20_events_from_raw.html')
    time.sleep(16)
    remote_drive.close()
