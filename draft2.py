import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "data_handle/msedgedriver.exe"
url = 'https://store.steampowered.com/'

driver = webdriver.Edge(PATH)
driver.get(url)

search_input = driver.find_element_by_id('store_nav_search_term')
if search_input is not None:
    search_input.send_keys('Sekiro')
    search_input.send_keys(Keys.RETURN)

apps_btn = driver.find_element_by_partial_link_text('Sekiro')
if apps_btn is not None:
    apps_btn.send_keys(Keys.RETURN)

temp = Select(driver.find_element_by_id('ageDay'))
if temp is not None:
    temp.select_by_visible_text('10')

temp = Select(driver.find_element_by_id('ageMonth'))
if temp is not None:
    temp.select_by_visible_text('October')

temp = Select(driver.find_element_by_id('ageYear'))
if temp is not None:
    temp.select_by_visible_text('2000')

temp = driver.find_element_by_link_text('View Page')
if temp is not None:
    temp.send_keys(Keys.RETURN)
#

#
# pwd_input = driver.find_element_by_id('0_signup_shop_name')
# if email_input is not None:
#     email_input.send_keys('testabc shop')
#
# skip_btn = driver.find_element_by_xpath('//button[text()="Skip"]')
# if skip_btn is not None:
#     skip_btn.send_keys(Keys.RETURN)
#
# fname_input = driver.find_element_by_id('PolarisTextField3')
# if fname_input is not None:
#     fname_input.send_keys('Frank')
#
# lname_input = driver.find_element_by_id('PolarisTextField4')
# if lname_input is not None:
#     lname_input.send_keys('Moss')
#
# adr_input = driver.find_element_by_id('PolarisTextField5')
# if adr_input is not None:
#     adr_input.send_keys('27 Lang Street')
#
# city_input = driver.find_element_by_id('PolarisTextField7')
# if city_input is not None:
#     city_input.send_keys('Ha Noi')
#
# country_input = driver.find_element_by_id('PolarisSelect1')
# if country_input is not None:
#     country_input.send_keys('Ha Noi')
#
# postcode_input = driver.find_element_by_id('PolarisTextField8')
# if postcode_input is not None:
#     postcode_input.send_keys('100000')
#
# postcode_input = driver.find_element_by_id('PolarisTextField1')
# if postcode_input is not None:
#     postcode_input.send_keys('+84 3913 920 123')
#
# tostore_btn = driver.find_element_by_xpath('//button[text()="Enter my store"]')
# if tostore_btn is not None:
#     tostore_btn.send_keys(Keys.RETURN)
#
# apps_btn = driver.find_element_by_link_text('Apps')
# if apps_btn is not None:
#     apps_btn.send_keys(Keys.RETURN)