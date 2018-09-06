#!/usr/bin/env
# -*- coding:utf8 -*-
# @author:Jiangzh

#!/usr/bin/env
# -*- coding:utf8 -*-
# @author:Jiangzh

import requests
from bs4 import BeautifulSoup
import  os
import time
from selenium import webdriver

class commontool():
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/68.0.3440.106 Safari/537.36'}
        self.url = 'https://unsplash.com/'
        self.folder_path = 'E:\picture'

    def request_Picture(self,url):
        r = requests.get(url,headers=self.headers)
        print(r)
        return r

    def mkdir(self,path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名称为',path,'的文件夹！')
            os.makedirs(path)
        else:
            print(path,'该文件夹已经存在！')

    def save_img(self,url,name):
        print('start save Pictrue...')
        img = self.request_Picture(url)
        time.sleep(5)
        file_name = name+'.jpg'
        f = open(file_name,'ab')
        f.write(img.content)
        f.close()

    def get_pic(self):
        print('start request...')
        driver = webdriver.Chrome('G:\chromedriver_win32\chromedriver.exe')
        driver.get(self.url)
        self.scroll_down(driver=driver,times=4)
        all_a = BeautifulSoup(driver.page_source,'lxml').find_all('img',class_='_2zEKz')
        self.mkdir(self.folder_path)
        os.chdir(self.folder_path)
        i=1
        for a in all_a:
            img_url = a['src']
            print(img_url)
            self.save_img(img_url,str(i))
            i+=1


    def scroll_down(self,driver,times):
        for i in range(times):
            print("start action",str(i+1),"seconds")
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            print("第",str(i+1),"次下拉操作执行完毕")
            print("第",str(i+1),"次等待网页加载")
            time.sleep(20)
