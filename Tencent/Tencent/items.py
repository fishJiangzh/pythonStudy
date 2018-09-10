# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    positionname = scrapy.Field() #职位名
    positionlink = scrapy.Field() #详情连接
    positionType = scrapy.Field() #职位类别
    peopleNum = scrapy.Field()    #招聘人数
    workLocation = scrapy.Field() #工作地点
    publishTime = scrapy.Field()  #发布时间