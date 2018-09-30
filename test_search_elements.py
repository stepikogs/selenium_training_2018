__author__ = 'George Stepiko'

from helpers import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_admin_headers(my_driver):
    driver = my_driver()
    driver.get('http://localhost/litecart/admin')
    WebDriverWait(driver, 10).until(ec.title_is("My Store"))
    login(wd=driver)
    # get menu items as list
    main_menu = get_items(driver, '#app-')
    # iterate menu
    for i in range(len(main_menu)):
        # get sub-menu as list (same function)
        item = get_items(driver, '#app-')[i]  # next element from known length
        item.click()                          # click it to open sub-menu if any
        sub_menu = get_items(driver, 'ul.docs li')  # check sub-menu
        if len(sub_menu) == 0:
            assert driver.find_elements_by_css_selector('h1')  # if no sub-menu - check header
        else:
            for k in range(len(sub_menu)):   # iterate sub-menu with checking of headers
                subber = get_items(driver, 'ul.docs li')[k]
                subber.click()
                assert driver.find_elements_by_css_selector('h1')
