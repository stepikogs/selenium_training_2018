__author__ = 'George Stepiko'

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# temp structure to refactor!

browsers_to_test = (
    'chrome',
    'ie',
    'firefox',
    'jeegurda'   # just to check incorrect browser option
)


@pytest.fixture
def my_driver(request):
    def browser(br='chrome'):
        if br.lower() == 'chrome':
            wd = webdriver.Chrome()
        elif br.lower() == 'firefox':
            wd = webdriver.Firefox(capabilities={"marionette": False})
        elif br.lower() == 'ie':
            wd = webdriver.Ie()
        else:
            print('Incorrect browser requested. Running in Chrome instead.')
            wd = webdriver.Chrome()
        print(wd.capabilities)
        request.addfinalizer(wd.quit)
        return wd
    return browser


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


# service
def login(wd, username="admin", password="admin"):
    wd.find_element_by_name("username").click()
    wd.find_element_by_name("username").clear()
    wd.find_element_by_name("username").send_keys(username)
    wd.find_element_by_name("password").click()
    wd.find_element_by_name("password").clear()
    wd.find_element_by_name("password").send_keys(password)
    wd.find_element_by_name("login").click()
