from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pytest
import pytest_dependency
import pytest_order
import pytest_html
import allure


@pytest.mark.order(1)
def test_add_item_miss(browser_admin_inside):
    cat = browser_admin_inside.find_element(By.CLASS_NAME, 'collapsed')
    cat.click()
    sleep(2)
    lis_pro = browser_admin_inside.find_element_by_id('collapse1').find_elements_by_tag_name('li')
    lis_pro[1].click()
    sleep(2)
    with pytest.raises(NoSuchElementException):
        exx = browser_admin_inside.find_element_by_xpath(("//img[@alt='Example']"))

@pytest.mark.order(2)
def test_add_item_example(browser_admin_inside):
    cat = browser_admin_inside.find_element_by_class_name('collapsed')
    cat.click()
    sleep(2)
    lis_pro = browser_admin_inside.find_element_by_id('collapse1').find_elements_by_tag_name('li')
    lis_pro[1].click()
    sleep(2)
    browser_admin_inside.find_element_by_class_name('btn-primary').click()
    sleep(2)
    prod_name = browser_admin_inside.find_element_by_name('product_description[1][name]')
    prod_name.send_keys('Example')
    meta_name = browser_admin_inside.find_element_by_name('product_description[1][meta_title]')
    meta_name.send_keys('Example')
    browser_admin_inside.find_element_by_link_text('Data').click()
    model = browser_admin_inside.find_element_by_id('input-model')
    model.send_keys('Example')
    browser_admin_inside.find_element_by_class_name('btn-primary').click()
    sleep(2)

def test_edit_item(browser_admin_inside):
    cat = browser_admin_inside.find_element_by_class_name('collapsed')
    cat.click()
    sleep(2)
    lis_pro = browser_admin_inside.find_element_by_id('collapse1').find_elements_by_tag_name('li')
    lis_pro[1].click()
    browser_admin_inside.find_element_by_css_selector('#form-product > div > table > tbody > tr:nth-child(3) > td:nth-child(8) > a > i').click()
    field = browser_admin_inside.find_element_by_class_name('note-editable')
    field.click()
    field.send_keys('Some description about item')
    browser_admin_inside.find_element_by_css_selector('#content > div.page-header > div > div > button').click()
    sleep(1)
    confirm = browser_admin_inside.find_element_by_class_name('alert-dismissible')
    assert confirm.text.strip() == 'Success: You have modified products!\n×'
    sleep(2)


def test_remove_item(browser_admin_inside):
    cat = browser_admin_inside.find_element_by_class_name('collapsed')
    cat.click()
    sleep(2)
    lis_pro = browser_admin_inside.find_element_by_id('collapse1').find_elements_by_tag_name('li')
    lis_pro[1].click()
    sleep(2)
    browser_admin_inside.find_element_by_css_selector(
        '#form-product > div > table > tbody > tr:nth-child(3) > td:nth-child(1) > input[type=checkbox]').click()
    sleep(2)
    browser_admin_inside.find_element_by_class_name('btn-danger').click()
    Alert(browser_admin_inside).accept()
    sleep(1)
