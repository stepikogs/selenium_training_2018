__author__ = 'George Stepiko'

import pytest
from helpers import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


browsers_to_test = (
    'chrome',
    'ie',
    'firefox',
    'firefox_nght',
    'jeegurda'   # just to check incorrect browser option
)


def test_example(my_driver):
    driver = my_driver()
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnK").click()
    WebDriverWait(driver, 10).until(ec.title_is("webdriver - Google Search"))


@pytest.mark.parametrize('brsr', browsers_to_test,
                         ids=browsers_to_test)
def test_login(my_driver, brsr):                               # no checks as while during task 3
    driver = my_driver(brsr)
    driver.get('http://localhost/litecart/admin')
    login(wd=driver)
