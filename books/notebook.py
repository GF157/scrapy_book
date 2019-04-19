import scrapy
import requests
from bs4 import BeautifulSoup
from scrapy import Request
from books.items import BooksItem


def get_links_info():
    urls = []
    list_view = 'https://book.douban.com/tag/%E4%BA%92%E8%81%94%E7%BD%91'
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    for link in soup.select(' div.info > h2 > a'):
        urls.append(link.get('href'))

    return urls
i=1

class NewsSpider(scrapy.Spider):
    name = 'content'
    allowed_domains = ['douban.com']
    start_urls =['https://book.douban.com/subject/6709783/']



    def parse(self, response):
        # items = []
        # item = BooksItem()
        # item['summary'] =response.xpath('normalize-space(//span[@class="all hidden"]//div[@class="intro"]').extract()[0]
        # item['author']=response.xpath('normalize-space(//span[@class="all hidden "]//div[@class="intro"])').extract()[0]
        # items.append(item)
        # print(items)


        urls = get_links_info()

        print(response.url)
        summary = response.xpath('normalize-space(//span[@class="all hidden"]//div[@class="intro"])').extract()[0]
        author = response.xpath('normalize-space(//span[@class="all hidden "]//div[@class="intro"])').extract()[0]
        data = {
            'summary':summary,
            'author' :author
        }
        yield (data)


        yield Request(urls[i])
        i+=1


import requests


jar = requests.cookies.RequestsCookieJar()
jar.set('bid', 'ehjk9OLdwha', domain='.douban.com', path='/')
jar.set('11', '25678', domain='.douban.com', path='/')
url = 'https://book.douban.com/tag/互联网'
r = requests.get(url, cookies=jar)
print(r.text)


#添加cookie请求网页

import scrapy
from scrapy.conf import settings #从settings文件中导入Cookie，这里也可以室友from scrapy.conf import settings.COOKIE

class DemoSpider(scrapy.Spider):
    name = "booktest"
    #allowed_domains = ["csdn.com"]
    start_urls = ['https://book.douban.com/tag/%E4%BA%92%E8%81%94%E7%BD%91']
    cookie = settings['COOKIE']  # 带着Cookie向网页发请求\
    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0],headers=self.headers,cookies=self.cookie)# 这里带着cookie发出请求

    def parse(self, response):
        print (response.body)



#爬取列表信息
 # names = response.xpath('').extract()
            # information = response.xpath(
            #     '//div[@id="wrapper"]//li[@class="subject-item"]//div[@class="pub"]/text()').extract_first().replace('\n','').strip()
            # score = response.xpath(
            #     '//div[@id="wrapper"]//li[@class="subject-item"]//div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()
            # number = response.xpath(
            #     '//div[@id="wrapper"]//li[@class="subject-item"]//div[@class="star clearfix"]/span[@class="pl"]/text()').extract()
            # urls= response.xpath('//h2/a/@href').extract()
            # for item in zip(names, information, score, number,urls):
            #     yield {
            #         "书名": item[0],
            #         "图书信息": item[1],
            #         "评分": item[2],
            #         "评分人数": item[3],
            #         "图书链接": item[4]
            #     }
            # return items