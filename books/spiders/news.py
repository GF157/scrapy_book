# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from string import  punctuation
from books.items import BooksItem
# class NewsSpider(scrapy.Spider):
#     name = 'news'
#     allowed_domains = ['douban.com']
#     start_urls = ['https://book.douban.com/tag/%E4%BA%92%E8%81%94%E7%BD%91']
#
#
#
#     def parse(self, response):
#         print(response.url)
#         items=[]
#         for book in response.xpath('//li[@class="subject-item"]'):
#             #创建item字段对象，用来存储信息
#             item = BooksItem()
#             item['name']= book.xpath('./div[@class="info"]//a/text()').extract()[0].replace('\n', '').strip()
#             item['information']=book.xpath('./div[@class="info"]/div[@class="pub"]/text()').extract_first().replace('\n', '').strip()
#             item['score']=book.xpath('./div[@class="info"]/div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()
#             item['number']=book.xpath('./div[@class="info"]/div[@class="star clearfix"]/span[@class="pl"]/text()').extract_first().replace('\n', '').strip()
#             item['url']=book.xpath('./div[@class="info"]//a/@href').extract_first().replace('\n', '').strip()
#             items.append(item)
#
#         next = response.xpath('//span[@class="next"]/link/@href').extract_first()
#         if next != None:
#             next_url = 'https://book.douban.com' + next
#             yield Request(next_url)
#         print(items)
#         return items

import scrapy



class Spider(scrapy.Spider):
    name = 'news'
    allowed_domains = []

    def start_requests(self):

        url = 'http://httpbin.org/get'

        for i in range(30):
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self,response):
        # ip=response.xpath('//div[@class="notediv"]/h1/span/text()').extract()[0]
        print(response.text)
