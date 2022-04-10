# number
import re
# csv
import csv
# selenium
import selenium
from selenium import webdriver
# Prevent Pass Warnings
from selenium.webdriver.chrome.service import Service
# Prevent find_element Warnings
from selenium.webdriver.common.by import By

URL = 'https://www.eiass.go.kr/biz/base/info/perList.do?menu=biz&biz_gubn=M&sKey=ADDR'

# Selenium Error Code : 0x1F
# https://choihyuunmin.tistory.com/82
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches',["enable-logging"])       

# DeprecationWarning: executable_path has been deprecated, please pass in a Service object
driver_path = Service('C:\Selenium\chromedriver.exe')
driver = webdriver.Chrome(service=driver_path,options=chrome_options)
driver.get(url=URL)

search_vector = ['제주도','서귀포','제주특별자치도']

for key in search_vector:
       # Find Search Box
       # DeprecationWarning: find_element_by_css_selector is deprecated. search = driver.find_element_by_css_selector('#sVal')
       search = driver.find_element(by=By.CSS_SELECTOR,value='#sVal')
       # Clear Search Box
       search.clear()
       # Send Key to Search Box
       search.send_keys(key)
       # Search w/ Key
       search.submit()
       
       # Find Total Number
       total = driver.find_element(by=By.CSS_SELECTOR,value='.tbl01_wrap > span')
       # Get Text
       total_text = total.get_attribute('innerText')
       # Translate to Number
       total_number = re.sub(r'[^0-9]','',total_text)
       
       if total_number == 0:
              break
       
       # Find Total Page Number
       total_page = int(total_number)//10
       
       for page in range(total_page):
              URL_ = URL + '&pn=' + str(page+1)
              print(URL_)
       
       print(key+"의 값은 : "+total_number)
driver.quit()       
