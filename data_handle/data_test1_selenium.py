import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "msedgedriver.exe"
url = 'http://45.79.43.178/source_carts/wordpress/wp-admin'

driver = webdriver.Edge(PATH)
driver.get(url)
print(driver.title)

user = driver.find_element_by_id('user_login')
password = driver.find_element_by_id('user_pass')
login_btn = driver.find_element_by_id('wp-submit')

user.send_keys('admin')
time.sleep(1)
password.send_keys('123456aA')
time.sleep(1)
login_btn.send_keys(Keys.RETURN)
# time.sleep(30)

WebDriverWait(driver, 10).until(EC.staleness_of(user))
username = driver.find_element_by_class_name('display-name').text
print(username)
# driver.quit()