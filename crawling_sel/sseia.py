import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# chromedriver 해당 경로
drPath = '../../../../../Selenium/chromedriver'

driver =webdriver.Chrome(executable_path=drPath)

URL = 'https://www.eiass.go.kr/biz/base/info/perList.do?menu=biz&biz_gubn=M'

sVal = ['제주도','서귀포','제주특별자치도']

URL_ = URL + '&sKey=ADDR&sVal=' + sVal[1]

driver.get(url=URL_)

try:
       total = EC.presence_of_element_located((By.CLASS_NAME, 'tbl01_wrap > span'))
finally:
       driver.quit()
       
print(total)