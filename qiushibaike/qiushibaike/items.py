# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiushibaikeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    content = scrapy.Field()
    agreed_number = scrapy.Field() #点赞数
    page_number = scrapy.Field() #页码
    id = scrapy.Field()


