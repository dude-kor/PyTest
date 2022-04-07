# 참조
# Python Selenium
# https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/
# Python PSSecutiryException
# https://hbesthee.tistory.com/1942

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://www.google.com'

driver =webdriver.Chrome(executable_path='../../../../../Selenium/chromedriver')
driver.get(url=URL)

print(driver.current_url)

driver.close()