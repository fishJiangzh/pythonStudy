#!/usr/bin/env
# -*- coding:utf8 -*-
# @author:Jiangzh

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('G:\chromedriver_win32\chromedriver.exe')
driver.get('http://www.baidu.com')
elem = driver.find_element_by_name('wd')
elem.clear()
elem.send_keys('江芝怀')
elem.send_keys(Keys.RETURN)
# assert 'ab' not   in driver.page_source
print(driver.get_cookies())
driver.close()
