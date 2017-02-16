# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .items import QiushibaikeItem

class QiushibaikePipeline(object):
    def process_item(self, item, spider):
        pass
