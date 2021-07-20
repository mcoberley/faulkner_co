# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from os import name
import scrapy

class WarrantItem(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()
    date = scrapy.Field()
    charges = scrapy.Field()

class ChildSupportOffenderItem(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()
    date = scrapy.Field()
    bond = scrapy.Field()
    charges = scrapy.Field()

class InmateItem(scrapy.Item):
    name = scrapy.Field()
    booking_number = scrapy.Field()
    age = scrapy.Field()
    gender = scrapy.Field()
    race = scrapy.Field()
    arresting_agency = scrapy.Field()
    booking_date = scrapy.Field()
    release_date = scrapy.Field()
    charges = scrapy.Field()
    vinelink = scrapy.Field()