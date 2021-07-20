import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SexOffendersSpider(CrawlSpider):
    name = 'sex_offenders'
    allowed_domains = ['fcso.ar.gov']
    start_urls = ['https://www.fcso.ar.gov/sex_offenders.php']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    def get_link(self, response):
        pass