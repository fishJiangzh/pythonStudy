#!/usr/bin/env
# -*- coding:utf8 -*-
# @author:Jiangzh

import requests
from bs4 import BeautifulSoup
import  os

import time

# headers = url = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                                       'Chrome/68.0.3440.106 Safari/537.36'}
# r = requests.get(url, headers=headers)
#
# all_a = BeautifulSoup(r.text,'lxml').find_all('a',class_='_2Mc8_')
#
# for a in all_a:
#     print(a['href'])

class BeautifulPicture():
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
        r = requests.get(self.url)
        all_a = BeautifulSoup(r.text,'lxml').find_all('a',class_='_2Mc8_')
        self.mkdir(self.folder_path)
        os.chdir(self.folder_path)
        for a in all_a:
            img_str = a['title']
            img_url = 'https://unsplash.com'+a['href']
            print(img_url)
            self.save_img(img_url,img_str)























# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html_doc,'lxml')
# find = soup.find('p')
# print("find's return type is",type(find))
# print("find's content is",find)
# print("find's Tag name is",find.name)
# print("find's Attribute(class) is",find['class'])
# print('NavigableString is',find.string)
