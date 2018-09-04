#!/usr/bin/env
# -*- coding:utf8 -*-
# @author:Jiangzh

import requests
import os
from selenium import webdriver
from bs4 import BeautifulSoup

class newcommon():
    def __init__(self):
        self.init_url='https://music.163.com/#/artist/album?id=8325&limit=27&offset=0'

    def request(self,url):
        r = requests.get(url)
        return  r

    def mkdir(self,path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            print("创建文件夹成功：",path)
            return True
        else:
            print('已经存在文件夹：',path)
            return False

    def get_files(self,path):
         files = os.listdir(path)

    def save_img(self,url,name):
        img= self.request(url)
        f = open(name+'.jpg','ab')
        f.write(img.content)
        f.close()


    def spider(self):
        print('start')
        path = 'E:\picture'
        self.mkdir(path)
        os.chdir(path)

        file_name = self.get_files(path)
        driver = webdriver.Chrome('G:\chromedriver_win32\chromedriver.exe')
        driver.get(self.init_url)
        driver.switch_to_frame("g_iframe")
        html = driver.page_source
        all_li = BeautifulSoup(html,'lxml').find(id='m-song-module').find_all('li')
        i=1
        for li in all_li:
            img = li.find('img')['src']
            name = li.find('p',class_='dec dec-1 f-thide2 f-pre')['title']
            date = li.find('span',class_='s-fc3').get_text()
            end_pos = img.index('?')
            img = img[:end_pos]
            if name+'.jpg' in file_name:
                print("已经存在...")
            else:
                print(i)
                self.save_img(img,name)
                i+=1

        driver.close()
