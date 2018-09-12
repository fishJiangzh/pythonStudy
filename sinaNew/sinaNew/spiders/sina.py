# -*- coding: utf-8 -*-
import scrapy
import os
from sinaNew.items import SinanewItem



class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        items = []
        parentUrls  = response.xpath('//div[@id="tab01"]/div/h3/a/@href').extract()
        parentTitle = response.xpath('//div[@id="tab01"]/div/h3/a/text()').extract()

        subUrls  = response.xpath('//div[@id="tab01"]/div/ul/li/a/@href').extract()
        subTitle = response.xpath('//div[@id="tab01"]/div/ul/li/a/text()').extract()
        os.chdir('E:\picture')

        for i in range(0,len(parentTitle)):
            parentFilename = "./Data/"+parentTitle[i]

            if(not os.path.exists(parentFilename)):
                os.makedirs(parentFilename)

            for j in range(0,len(subUrls)):
                item = SinanewItem()
                item['parentTitle'] = parentTitle[i]
                item['parentUrls']  = parentUrls[i]

                if_belong = subUrls[j].startswith(parentUrls[i])

                if(if_belong):
                    subFilename = parentFilename +'/'+subTitle[j]

                    if(not os.path.exists(subFilename)):
                        os.makedirs(subFilename)

                    item['subTitle'] = subTitle[j]
                    item['subUrls']  = subUrls[j]
                    item['subFilename'] = subFilename

                    items.append(item)

        for item in items:
            yield scrapy.Request(url=item['subUrls'],meta={'meta_1':item},callback=self.sencond_parse)



    def sencond_parse(self,response):
        meta_1 = response.meta['meta_1']
        sonUrls = response.xpath('//a/@href').extract()
        items = []

        for i in range(0,len(sonUrls)):

            if_belong = sonUrls[i].endswith('.shtml') and sonUrls[i].startswith(meta_1['parentUrls'])

            if(if_belong):
                print(i)
                print(sonUrls[i])
                item = SinanewItem()
                item['parentUrls'] = meta_1['parentUrls']
                item['parentTitle'] = meta_1['parentTitle']
                item['subUrls'] = meta_1['subUrls']
                item['subTitle'] = meta_1['subTitle']
                item['subFilename'] = meta_1['subFilename']
                item['sonUrls'] = sonUrls[i]
                items.append(item)

        for item in items:
            yield scrapy.Request(url=item['sonUrls'],meta={'meta_2':item},callback=self.detall_parse)


    def detall_parse(self,response):
        item = response.meta['meta_2']
        content = ""
        head = response.xpath('//h1[@class="main-title"]/text()')
        content_list = response.xpath('//div[@id="article"]/p/text()').extract()

        for content_one in content_list:
            content +=content_one

        item['head'] = head.extract()[0]
        item['content'] = content

        yield item

