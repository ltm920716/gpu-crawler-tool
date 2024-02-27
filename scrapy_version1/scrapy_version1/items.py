# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyVersion1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class GpuInfoItem(scrapy.Item):
    name = scrapy.Field()
    gpu = scrapy.Field()
    scale = scrapy.Field()
    gpu_ram = scrapy.Field()
    vcpus = scrapy.Field()
    cpu_info = scrapy.Field()
    ram = scrapy.Field()
    storage = scrapy.Field()
    bandwidth = scrapy.Field()
    type = scrapy.Field()
    regions = scrapy.Field()
    hour_price = scrapy.Field()
    month_price = scrapy.Field()
    year_price = scrapy.Field()
    account = scrapy.Field()