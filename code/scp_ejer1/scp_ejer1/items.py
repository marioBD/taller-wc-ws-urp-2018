# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScpEjer1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    titulo= scrapy.Field()
    autor = scrapy.Field()
    resumen = scrapy.Field()
    editor = scrapy.Field()
    year = scrapy.Field()
