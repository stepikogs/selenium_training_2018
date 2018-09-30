__author__ = 'George Stepiko'

from helpers import *


def test_countries_extended_sort(my_driver):
    driver = my_driver()
    admin_login(wd=driver)
    driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
    countries_list = get_items(driver, 'table.dataTable .row')
    extracted_list = []
    with_zones = []
    for item in countries_list:
        extracted_list.append(item.find_element_by_css_selector('td:nth-child(5) > a').text)
        if item.find_element_by_css_selector('td:nth-child(6)').text is not '0':   # extract with zones
            with_zones.append(item.find_element_by_css_selector('td:nth-child(5) > a').get_attribute('href'))
            pass
    assert len(countries_list) == len(extracted_list)  # service: extraction check
    assert extracted_list == sorted(extracted_list)

    # work with zones sort
    extracted_zones = []
    zonez_list = []
    for country in with_zones:
        extracted_zones = []
        driver.get(country)
        zonez_list = get_items(driver, 'table#table-zones input[name*=name][type=hidden]')
        for zone in zonez_list:
            extracted_zones.append(zone.get_attribute('value'))
    assert len(zonez_list) == len(extracted_zones)
    assert extracted_zones == sorted(extracted_zones)
