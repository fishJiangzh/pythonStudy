#!/usr/bin/env
# -*- coding:utf8 -*-
# @author:Jiangzh

# import urllib.request
#
# headers = {
# "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
# "accept-encoding": "gzip, deflate, br",
# "accept-language": "zh-CN,zh;q=0.9",
# "cache-control": "max-age=0",
# "referer": "https://www.zhihu.com/signup?next=%2F",
# "upgrade-insecure-requests":" 1",
# "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
# "cookie" : "tgw_l7_route=5bcc9ffea0388b69e77c21c0b42555fe; _xsrf=shLKtlo4CfawphyvzuIdPoyjzj5iYtJs;"
#            " _zap=b586d28c-cb6b-49f0-87b9-2394a4e208d5; d_c0=\"AFAmSaC5LA6PTu5ccWrakk0LOFNrsULkwNs=|1536299619\"; "
#            "capsion_ticket=\"2|1:0|10:1536299625|14:capsion_ticket|44:MzYyOWJmMGU0YjExNGM2YjhhMDAwY2FkYmFhZGVkNTU=|741f95da783204e6839ffcafdf2bc94c1d4dee31da6e8a802b5dd61eb7d6b6b9\"; "
#            "z_c0=\"2|1:0|10:1536299632|4:z_c0|92:Mi4xSjRDZUF3QUFBQUFBOEtReG9Ma3NEaVlBQUFCZ0FsVk5jR0JfWEFDalA3LWFKSXRIRk9uMEhrUnJfUTROUGVtVXNR|aa92be1cf939c1cc34538300349fba8a513bed95288af9a8ce5d268bb06ade1b\";"
#            " q_c1=7ae4b5c394944e70a44e8f9647373609|1536299634000|1536299634000"
# }
#
# req = urllib.request.Request("http://www.zhihu.com/",headers=headers,method="POST")
#
# print(req)
# r = urllib.request.urlopen(req)
#
# print(r.read())



import urllib.request
import urllib.parse
import http.cookiejar

cookie = http.cookiejar.CookieJar()

cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(cookie_handler)

opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')]


data = {"email":"jiangzhihuai9420@163.com","password":"jzh881123"}

postdata = urllib.parse.urlencode(data).encode(encoding='UTF8')

print(postdata)

request = urllib.request.Request("http://www.renren.com/PLogin.do",data=postdata)

opener.open(request)

req = opener.open("http://www.renren.com/410049765/profile")

print(req.read())
print("complete!")


