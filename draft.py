import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mail = 'trieuhaipham1998@gmail.com'
pwd = '123!@#qwe'

PATH = "data_handle/msedgedriver.exe"
url = 'https://shopify.com'

driver = webdriver.Edge(PATH)
driver.get(url)

new_btn = driver.find_element_by_xpath('//button[text()="Start free trial"]')
if new_btn is not None:
    new_btn.send_keys(Keys.RETURN)

email_input = driver.find_element_by_id('0_signup_email')
if email_input is not None:
    email_input.send_keys(mail)

pwd_input = driver.find_element_by_id('0_signup_password')
if email_input is not None:
    email_input.send_keys(pwd)

pwd_input = driver.find_element_by_id('0_signup_shop_name')
if email_input is not None:
    email_input.send_keys('testabc shop')

skip_btn = driver.find_element_by_xpath('//button[text()="Skip"]')
if skip_btn is not None:
    skip_btn.send_keys(Keys.RETURN)

fname_input = driver.find_element_by_id('PolarisTextField3')
if fname_input is not None:
    fname_input.send_keys('Frank')

lname_input = driver.find_element_by_id('PolarisTextField4')
if lname_input is not None:
    lname_input.send_keys('Moss')

adr_input = driver.find_element_by_id('PolarisTextField5')
if adr_input is not None:
    adr_input.send_keys('27 Lang Street')

city_input = driver.find_element_by_id('PolarisTextField7')
if city_input is not None:
    city_input.send_keys('Ha Noi')

country_input = driver.find_element_by_id('PolarisSelect1')
if country_input is not None:
    country_input.send_keys('Ha Noi')

postcode_input = driver.find_element_by_id('PolarisTextField8')
if postcode_input is not None:
    postcode_input.send_keys('100000')

postcode_input = driver.find_element_by_id('PolarisTextField1')
if postcode_input is not None:
    postcode_input.send_keys('+84 3913 920 123')

tostore_btn = driver.find_element_by_xpath('//button[text()="Enter my store"]')
if tostore_btn is not None:
    tostore_btn.send_keys(Keys.RETURN)

apps_btn = driver.find_element_by_link_text('Apps')
if apps_btn is not None:
    apps_btn.send_keys(Keys.RETURN)

temp = driver.find_element_by_link_text('Manage private apps')
if temp is not None:
    temp.send_keys(Keys.RETURN)

temp = driver.find_element_by_link_text('Enable private app development')
if temp is not None:
    temp.send_keys(Keys.RETURN)

temp = driver.find_element_by_id('checkbox-74fb04734ddc21504f4e307d7d7afa83')
if not temp.get_attribute('checked'):
    temp.send_keys(Keys.RETURN)

temp = driver.find_element_by_id('checkbox-f2a4e596b6eba472a054999915097010')
if not temp.get_attribute('checked'):
    temp.send_keys(Keys.RETURN)

temp = driver.find_element_by_id('checkbox-bd7628049d89001d5ac203ec45290bab')
if not temp.get_attribute('checked'):
    temp.send_keys(Keys.RETURN)

temp = driver.find_element_by_link_text('Create private app')
if temp is not None:
    temp.send_keys(Keys.RETURN)

temp = driver.find_element_by_id('api_client_title')
if temp is not None:
    temp.send_keys('Test Shop')

temp = driver.find_element_by_id('api_client_contact_email')
if temp is not None:
    temp.send_keys(mail)

temp = driver.find_element_by_xpath('//button[text()="Show inactive Admin API permissions"]')
if temp is not None:
    temp.send_keys(Keys.RETURN)

temp = Select(driver.find_element_by_id('api_client[access_scope][analytics][authenticated]'))
if temp is not None:#1
    temp.select_by_visible_text('Read access')

temp = Select(driver.find_element_by_id('api_client[access_scope][assigned_fulfillment_orders][authenticated]'))
if temp is not None:#2
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][customers][authenticated]'))
if temp is not None:#3
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][discounts][authenticated]'))
if temp is not None:#4
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][draft_orders][authenticated]'))
if temp is not None:#5
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][files][authenticated]'))
if temp is not None:#6
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][fulfillments][authenticated]'))
if temp is not None:#7
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][gdpr_data_request][authenticated]'))
if temp is not None:#8
    temp.select_by_visible_text('Read access')

temp = Select(driver.find_element_by_id('api_client[access_scope][gift_cards][authenticated]'))
if temp is not None:#9
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][inventory][authenticated]'))
if temp is not None:#10
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][kit_skills][authenticated]'))
if temp is not None:#11
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][legal_policies][authenticated]'))
if temp is not None:#12
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][locations][authenticated]'))
if temp is not None:#13
    temp.select_by_visible_text('Read access')

temp = Select(driver.find_element_by_id('api_client[access_scope][marketing_events][authenticated]'))
if temp is not None:#14
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][merchant_managed_fulfillment_orders][authenticated]'))
if temp is not None:#15
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][online_store_navigation][authenticated]'))
if temp is not None:#16
    temp.select_by_visible_text('Read access')

temp = Select(driver.find_element_by_id('api_client[access_scope][online_store_pages][authenticated]'))
if temp is not None:#17
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][order_edits][authenticated]'))
if temp is not None:#18
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][orders][authenticated]'))
if temp is not None:#19
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][payment_terms][authenticated]'))
if temp is not None:#20
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][price_rules][authenticated]'))
if temp is not None:#21
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][product_listings][authenticated]'))
if temp is not None:#22
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][products][authenticated]'))
if temp is not None:#23
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][reports][authenticated]'))
if temp is not None:#24
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][resource_feedbacks][authenticated]'))
if temp is not None:#25
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][script_tags][authenticated]'))
if temp is not None:#26
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][shipping][authenticated]'))
if temp is not None:#27
    temp.select_by_visible_text('Read and write')

    temp = Select(driver.find_element_by_id('api_client[access_scope][locales][authenticated]'))
if temp is not None:#28
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][shopify_payments_accounts][authenticated]'))
if temp is not None:#29
    temp.select_by_visible_text('Read access')

temp = Select(driver.find_element_by_id('api_client[access_scope][shopify_payments_bank_accounts][authenticated]'))
if temp is not None:#30
    temp.select_by_visible_text('Read access')

temp = Select(driver.find_element_by_id('api_client[access_scope][shopify_payments_disputes][authenticated]'))
if temp is not None:#31
    temp.select_by_visible_text('Read access')

temp = Select(driver.find_element_by_id('api_client[access_scope][shopify_payments_payouts][authenticated]'))
if temp is not None:#32
    temp.select_by_visible_text('Read access')

temp = Select(driver.find_element_by_id('api_client[access_scope][content][authenticated]'))
if temp is not None:#33
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][themes][authenticated]'))
if temp is not None:#34
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][third_party_fulfillment_orders][authenticated]'))
if temp is not None:#35
    temp.select_by_visible_text('Read and write')

temp = Select(driver.find_element_by_id('api_client[access_scope][translations][authenticated]'))
if temp is not None:#36
    temp.select_by_visible_text('Read and write')

temp = driver.find_element_by_xpath('//button[text()="Save"]')
if temp is not None:
    temp.send_keys(Keys.RETURN)

temp = driver.find_element_by_xpath('//button[text()="Create app"]')
if temp is not None:
    temp.send_keys(Keys.RETURN)

temp = driver.find_element_by_xpath('//button[text()="Save"]')
if temp is not None:
    temp.send_keys(Keys.RETURN)

