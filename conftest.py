__author__ = 'George Stepiko'

import pytest
from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec



@pytest.fixture
def my_driver(request):
    def browser(br='chrome'):
        if br.lower() == 'chrome':
            wd = webdriver.Chrome()
        elif br.lower() == 'firefox':
            wd = webdriver.Firefox(capabilities={"marionette": False})
        elif br.lower() == 'firefox_nght':
            wd = webdriver.Firefox(firefox_binary="c:\\Program Files\\Firefox Nightly\\firefox.exe")
        elif br.lower() == 'ie':
            wd = webdriver.Ie()
        else:
            print('Incorrect browser requested. Running in Chrome instead.')
            wd = webdriver.Chrome()
        print(wd.capabilities)
        wd.implicitly_wait(5)
        request.addfinalizer(wd.quit)
        return wd
    return browser
