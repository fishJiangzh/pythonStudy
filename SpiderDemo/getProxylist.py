#!/usr/bin/env
# -*- coding:utf8 -*-
# @author:Jiangzh

import requests
from bs4 import  BeautifulSoup
import random

class Proxy():

    def getProxylist(self):
        Pr_list=[]
        for i in range(1,5):
            r = requests.get("https://www.kuaidaili.com/free/inha/"+str(i)+"/")
            all_tr = BeautifulSoup(r.text, 'lxml').find_all('tr')
            for tr in all_tr:
                all_td = tr.find_all('td')
                if all_td:
                    y = all_td[5].text.index("秒")
                    response_time = all_td[5].text[:y]
                    if(float(response_time)<1):
                        d = {all_td[3].text:all_td[0].text + ':'+ all_td[1].text}
                        Pr_list.append(d)
        return Pr_list

# if __name__ == '__main__':
#     proxy = Proxy()
#     polist = proxy.getProxylist()
#     print(polist.__len__())
#     po = random.choice(polist)
#     print(po)

