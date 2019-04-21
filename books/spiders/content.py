import scrapy
from books.items import BooksItem
from scrapy import Request
import re
import pymongo
import random
import time

client = pymongo.MongoClient('localhost', 27017)
book = client['book']
all = book['421_11']
tes = book['421_22']


class NewsSpider(scrapy.Spider):
    name = 'content'
    allowed_domains = ['douban.com']

    def start_requests(self):

        start_urls = [
            'https://book.douban.com/tag/%E4%BA%92%E8%81%94%E7%BD%91',  # 互联网
            'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B',  # 编程
            'https://book.douban.com/tag/%E4%BA%A4%E4%BA%92%E8%AE%BE%E8%AE%A1',  # 交互设计
            'https://book.douban.com/tag/%E7%AE%97%E6%B3%95',  # 算法
            'https://book.douban.com/tag/web',  # web
            'https://book.douban.com/tag/UE',  # UE
            'https://book.douban.com/tag/%E4%BA%A4%E4%BA%92',  # 交互
            'https://book.douban.com/tag/%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C',  # 神经网络
            'https://book.douban.com/tag/%E7%A8%8B%E5%BA%8F',  # 程序

        ]

        for url in start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = [
            'https://book.douban.com/tag/%E4%BA%92%E8%81%94%E7%BD%91',  # 互联网
            'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B',  # 编程
            'https://book.douban.com/tag/%E4%BA%A4%E4%BA%92%E8%AE%BE%E8%AE%A1',  # 交互设计
            'https://book.douban.com/tag/%E7%AE%97%E6%B3%95',  # 算法
            'https://book.douban.com/tag/web',  # web
            'https://book.douban.com/tag/UE',  # UE
            'https://book.douban.com/tag/%E4%BA%A4%E4%BA%92',  # 交互
            'https://book.douban.com/tag/%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C',  # 神经网络
            'https://book.douban.com/tag/%E7%A8%8B%E5%BA%8F',  # 程序
        ]

        result = (response.url.split('?')[0]) in urls

        ret = 'doings'
        item = BooksItem()

        # wait = round(random.uniform(1, 2), 2)
        # time.sleep(wait)
        # print("间隔时间:")
        # print(wait)


        if result:

            for href in response.xpath('//li[@class="subject-item"]/div[@class="info"]//h2//a/@href').extract():
                yield Request(href)
            print(response.url)
            # yield下一页链接
            next = response.xpath('//span[@class="next"]/link/@href').extract_first()
            if next != None:
                next_url = 'https://book.douban.com' + next
                yield Request(next_url)

        elif ret in response.url:
            item['url'] = response.url.split('/d',1)[0]
            try:
                item['read'] = response.xpath('//*[@id="collections_bar"]/span/a/text()').extract()[0]
                item['read'] = re.findall(r'\d*', item['read'])[0]
            except:
                print("No find read!")
                item['read'] = 0

            try:
                item['read_want'] = response.xpath('//*[@id="wishes_bar"]/span/a/text()').extract()[0]
                item['read_want'] = re.findall(r'\d*', item['read_want'])[0]

            except:
                print("No find read_want!")
                item['read_want'] = 0

            try:
                item['reading'] = response.xpath('//*[@id="doings_bar"]/span/text()').extract()[0]
                item['reading'] = re.findall(r'\d*', item['reading'])[0]
            except:
                print("No find reading!")
                item['reading'] = 0
            try:
                base_info = response.xpath('//div[@class="indent"]').extract()[0].replace('\n', '').replace(' ', '')
                item['ISBN'] = re.findall(r'isbn:</span>(\d*)<br>', base_info)[0]
            except:
                print('No find ISBN!')
                item['ISBN'] = 0
            try:
                item['author'] = re.findall(r"作者:(.*?)</span>", base_info, re.S)[0]
            except:
                print('No find 作者!')
                item['author'] = 0
            try:
                item['title'] = re.findall(r'书名:</span>(.*?)<br>', base_info)[0]
            except:
                item['title'] = 0
            try:
                item['press'] = re.findall(r'出版社:</span>(.*?)<br>', base_info)[0]
            except:
                item['press'] = 0
            try:
                item['trans'] = re.findall(r'译者:(.*?)</span>', base_info)[0]
            except:
                item['trans'] = 0
            try:
                date = re.findall(r'出版年:</span>(.*?)<br>', base_info)[0]
                item['publish_date'] = re.findall(r'\d*-\d+', date)[0]
            except:
                item['publish_date'] = 0
            try:
                item['score'] = response.xpath('//*[@id="content"]/div/div[1]/div[1]/div[1]/p/strong/text()').extract()[0]
            except:
                item['score'] = 0
            try:
                number = response.xpath('//*[@id="content"]/div/div[1]/h2/span/text()').extract()[0]
                item['number'] = re.findall(r'(\d*)', number)[0]
            except:
                item['number'] = 0
            try:
                item['image'] = response.xpath('//*[@id="content"]/div/div[2]/div[2]/a/img/@src').extract()[0]
            except:
                item['image'] = 0

            try:
                distr = response.xpath('//div[@class="rating_detail_star"]').extract()[0].replace('\n', '').replace(' ', '')
                part = re.compile("(\d*.\d*)%")
                item['one'] = part.findall(distr)[4]
                item['two'] = part.findall(distr)[3]
                item['three'] = part.findall(distr)[2]
                item['four'] = part.findall(distr)[1]
                item['five'] = part.findall(distr)[0]
            except:
                print('can not find distr')
                item['one'] = 0

            yield item
            print(item)
            # postitem = dict(item)
            # tes.insert(postitem)


        else:

            item['url'] = response.url
            try:
                item['title'] = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract()[0]
            except:
                print("No find title!")
                item['title'] = 0

            try:
                item['score'] = response.xpath('//div[@id="interest_sectl"]//strong/text()').extract()[0].replace(' ','')
            except:
                print("未找到评分")
                item['score'] = 0

            try:
                item['number'] = response.xpath('//div[@class="rating_sum"]//a//text()').extract()[0].replace('\n', '')
            except:
                print("未找到评分人数")
                item['number'] = 0

            base_info = response.xpath('//div[@id="info"]').extract()[0].replace('\n', '')

            try:
                author = re.findall(r"作者(.*?)</a>", base_info, re.S)[0]
                part = re.compile(r'">(.*)')
                item['author'] = part.findall(author)[0].replace(' ', '')
            except:
                print("No find author!")
                item['author'] = 0

            try:
                press = re.findall(r'出版社(.*?)<br>', base_info)[0]
                part = re.compile(r'</span>(.*)')
                press = part.findall(press)[0]
                item['press'] = press
            except:
                print("No find press!")
                item['press'] = 0


            try:
                publish_date = re.findall(r'出版年(.*?)<br>', base_info)[0]
                pat = re.compile(r'</span>(.*)')
                date = pat.findall(publish_date)[0]
                date = re.findall(r'(\d\d\d\d)', date)[0]
                item['publish_date'] = date
            except:
                print("No find date!")
                item['publish_date'] = 0

            item['ISBN'] = re.findall(r'ISBN:</span> (\d*)', base_info)[0]


            try:
                read = response.xpath('//div[@id="collector"]/p/a/text()').extract()
                item['reading'] = re.findall(r'(\d*)人在读', read)[0]
            except:
                print("reading find error!")
                item['reading'] = 0

            try:
                item['read'] = re.findall(r'(\d*)人读过', read)[0]
            except:
                print("read find error!")
                item['read'] = 0

            try:
                item['read_want'] = re.findall(r'(\d*)人想读', read)[0]
            except:
                print('read_want find error!')
                item['read_want'] = 0

            try:
                item['label']= response.xpath('//div[@id="db-tags-section"] /div[@class="indent"]/span/a/text()').extract()
            except:
                print("No label!")
                item['label'] = 0
            item['image'] = response.xpath('//*[@id="mainpic"]/a/img/@src').extract()[0]

            yield Request(response.url + 'doings')
            yield item
            print(item)

        # data={
        #     '书名' : item['title'],
        #     '作者' : item['author'],
        #     '评分' : item['score'],
        #     '评分人数': item['number'],
        #     '定价': item['price'],
        #     '出版社': item['press'],
        #     '出版年': item['publish_date'],
        #     '页数': item['pages'],
        #     'ISBN': item['ISBN'],
        #     '标签': item['label'],
        #     '读过的人': item['read'],
        #     '想读的人': item['read_want'],
        #     '在读的人': item['reading'],
        #     '内容简介':item['summary'],
        #     '作者简介':item['author_s'],
        #     '图书链接':item['url']
        # }

        #     postitem = dict(item)
        #     all.insert(postitem)

        # for items in all.find():
        #     yield items
