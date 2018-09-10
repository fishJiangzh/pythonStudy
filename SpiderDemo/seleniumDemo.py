#!/usr/bin/env
# -*- coding:utf8 -*-
# @author:Jiangzh


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('G:\chromedriver_win32\chromedriver.exe')
driver.get('http://www.renren.com')

driver.find_element_by_name('email').send_keys('jiangzhihuai9420@163.com')
driver.find_element_by_name('password').send_keys('jzh881123')


driver.find_element_by_id('login').click()

time.sleep(3)

driver.save_screenshot('renren.png')









