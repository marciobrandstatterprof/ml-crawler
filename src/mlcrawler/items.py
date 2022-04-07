# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MlcrawlerItem(scrapy.Item):
    title = scrapy.Field()
    seller = scrapy.Field()
    price = scrapy.Field()
    discount = scrapy.Field()
    old_price = scrapy.Field()
    shipping = scrapy.Field()
    link = scrapy.Field()
    
