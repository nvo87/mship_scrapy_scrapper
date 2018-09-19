# -*- coding: utf-8 -*-

import scrapy


class Product(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()