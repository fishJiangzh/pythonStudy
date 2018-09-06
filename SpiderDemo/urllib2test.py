#!/usr/bin/env
# -*- coding:utf8 -*-
# @author:Jiangzh

import urllib.request

httpproxy_handler = urllib.request.ProxyHandler({"HTTP": "111.40.84.73:9999"})
nullproxy_handler = urllib.request.ProxyHandler({})

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

print(response.read())
