__author__ = 'George Stepiko'

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# temp structure to refactor!


# fixtures
@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnK").click()
    WebDriverWait(driver, 10).until(ec.title_is("webdriver - Google Search"))


def test_login(driver):   # no checks as while during task 3
    driver.get('http://localhost/litecart/admin')
    login(wd=driver)


# service
def login(wd, username="admin", password="secret"):
    wd.find_element_by_name("username").click()
    wd.find_element_by_name("username").clear()
    wd.find_element_by_name("username").send_keys(username)
    wd.find_element_by_name("password").click()
    wd.find_element_by_name("password").clear()
    wd.find_element_by_name("password").send_keys(password)
    wd.find_element_by_name("login").click()
