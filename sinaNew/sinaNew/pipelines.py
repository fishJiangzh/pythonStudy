# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinanewPipeline(object):
    def process_item(self, item, spider):
        head = item['head']

        filename = head.replace('/','_')
        filename += ".txt"

        fp = open(item['subFilename']+'/'+filename,'w')
        fp.write(item['content'].replace(u'\xa0',u''))
        fp.close()

        return item
