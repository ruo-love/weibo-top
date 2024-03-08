# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboTopItem(scrapy.Item):
    title = scrapy.Field()  # '名称'
    link = scrapy.Field()  # '详情地址'
    desc = scrapy.Field()  # 'desc'
    pass
