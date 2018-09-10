#!/usr/bin/env
# -*- coding:utf8 -*-
# @author:Jiangzh


import requests

ssion = requests.session()

header =[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')]

data = {'email':'jiangzhihuai9420@163.com','password':'jzh881123'}

ssion.post("http://www.renren.com/PLogin.do",data=data)

response = ssion.get("http://www.renren.com/410049765/profile")

print(response.text)

