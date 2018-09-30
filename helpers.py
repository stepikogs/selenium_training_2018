__author__ = 'George Stepiko'

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

HOME = 'http://localhost/litecart/'
ODMEN = HOME + 'admin'


def go_home(wd):
    wd.get(HOME)
    WebDriverWait(wd, 10).until(ec.title_is("Online Store | My Store"))


def go_admin(wd):
    wd.get(ODMEN)
    WebDriverWait(wd, 10).until(ec.title_is("My Store"))


def login(wd, username="admin", password="admin"):
    wd.find_element_by_name("username").click()
    wd.find_element_by_name("username").clear()
    wd.find_element_by_name("username").send_keys(username)
    wd.find_element_by_name("password").click()
    wd.find_element_by_name("password").clear()
    wd.find_element_by_name("password").send_keys(password)
    wd.find_element_by_name("login").click()


def admin_login(wd):
    go_admin(wd)
    login(wd)


def get_items(context, locator):
    # if context:
    #     lister = context.find_elements_by_css_selector('{}'.format(locator))
    return context.find_elements_by_css_selector('{}'.format(locator))
