# -*- coding: utf-8 -*-
import scrapy
from FilmDemo.items import  FilmdemoItem


class FilmspiderSpider(scrapy.Spider):
    name = 'FilmSpider'
    allowed_domains = ['movie.douban.com']
    offset = 0
    url = "https://movie.douban.com/top250?start="
    start_urls = [url + str(offset)]
    # start_urls = ['https://movie.douban.com/chart']


    def parse(self, response):
        # pass

        item = FilmdemoItem()
        movies = response.xpath('//div[@class="info"]')

        for movie in movies:
            item['title'] = movie.xpath('.//span[@class="title"][1]/text()').extract()[0]

            item['bd'] = movie.xpath('.//div[@class="bd"]/p/text()').extract()[0]

            item['star'] = movie.xpath('.//span[@class="rating_num"]/text()').extract()[0]

            quote = movie.xpath('.//p[@class="quote"]/span/text()').extract()

            if len(quote)!=0:
                item['quote'] = quote[0]

            yield item

        if self.offset<60:
            self.offset += 25
            yield scrapy.Request(url=self.url+str(self.offset),callback=self.parse)


        print('-----')
        print('complete...')
