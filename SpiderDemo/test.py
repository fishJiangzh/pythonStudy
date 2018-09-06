#!/usr/bin/env
# -*- coding:utf8 -*-
# @author:Jiangzh

# from common import commontool
#
# if __name__ == '__main__':
#     beauty = commontool()
#     beauty.get_pic()

import os

# for root,dirs,files in os.walk('E:\picture'):
#     for file in files:
#         print(file)

for file in os.listdir('E:\picture'):
    print(file)
