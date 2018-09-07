#!/usr/bin/env
# -*- coding:utf8 -*-
# @author:Jiangzh

import urllib.request
import random
from getProxylist import Proxy

p = Proxy()
pro = p.getProxylist()
print(pro)
# proxy_list = [{"HTTP": "183.154.215.78:9000"},
#               {"HTTP": "180.118.134.103:9000"},
#               {"HTTP": "114.235.22.251:9000"},
#               {"HTTP": "115.223.210.203:9000"},
#               {"HTTP": "223.150.39.128:9000"},
#               {"HTTP": "180.118.128.138:9000"}]

proxy = random.choice(pro)
print(proxy)
httpproxy_handler = urllib.request.ProxyHandler(proxy)
nullproxy_handler = urllib.request.ProxyHandler({})

# # 构建具有一个私密代理IP的Handler，其中user为账户，passwd为密码
# httpproxy_handler = urllib.request.ProxyHandler({"http" : "user：passwd@124.88.67.81:80"})

proxySwitch = True

if proxySwitch:
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)

request = urllib.request.Request("http://www.baidu.com/")

# 使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理。
response = opener.open(request)

# 就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
# urllib2.install_opener(opener)
# response = urlopen(request)

# print(response.read())
print("complete")
