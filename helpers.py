__author__ = 'George Stepiko'


def login(wd, username="admin", password="admin"):
    wd.find_element_by_name("username").click()
    wd.find_element_by_name("username").clear()
    wd.find_element_by_name("username").send_keys(username)
    wd.find_element_by_name("password").click()
    wd.find_element_by_name("password").clear()
    wd.find_element_by_name("password").send_keys(password)
    wd.find_element_by_name("login").click()


def get_items(context, locator):
    # if context:
    #     lister = context.find_elements_by_css_selector('{}'.format(locator))
    return context.find_elements_by_css_selector('{}'.format(locator))
