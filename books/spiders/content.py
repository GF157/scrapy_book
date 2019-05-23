import scrapy
from books.items import BooksItem
from scrapy import Request
import re
import pymongo
from urllib import parse
from scrapy_redis.spiders import RedisCrawlSpider
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

client = pymongo.MongoClient('localhost', 27017)
book = client['book']
all = book['tag']
# tes = book['05082']


class NewsSpider(scrapy.Spider):
    name = 'content'
    # redis_key = 'myspider:start_urls'
    allowed_domains = ['douban.com']

    # selenium 无头模式
    # def __init__(self):
    #     chrome_options = Options()
    #     chrome_options.add_argument('--headless')
    #     self.browser = webdriver.Chrome(chrome_options=chrome_options)
    #     self.browser.set_page_load_timeout(30)
    #
    # def closed(self, spider):
    #     print("spider closed")
    #     self.browser.close()

    def start_requests(self):

        start_urls = [

                        # 'https://book.douban.com/tag/%E9%80%9A%E4%BF%A1',  # 通信
                        # 'https://book.douban.com/tag/%E7%A7%91%E6%8A%80',  # 科技
                        # 'https://book.douban.com/tag/%E7%94%A8%E6%88%B7%E4%BD%93%E9%AA%8C',  # 用户体验
                        # 'https://book.douban.com/tag/%E4%BA%92%E8%81%94%E7%BD%91',  # 互联网
                        # 'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B',  # 编程
                        # 'https://book.douban.com/tag/%E4%BA%A4%E4%BA%92%E8%AE%BE%E8%AE%A1',  # 交互设计
                        # 'https://book.douban.com/tag/%E7%AE%97%E6%B3%95',  # 算法
                        # 'https://book.douban.com/tag/web',  # web
                        # 'https://book.douban.com/tag/UE',  # UE
                        # 'https://book.douban.com/tag/%E4%BA%A4%E4%BA%92',  # 交互
                        # 'https://book.douban.com/tag/%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C',  # 神经网络
                        # 'https://book.douban.com/tag/%E7%A8%8B%E5%BA%8F',  # 程序
                        # 'https://book.douban.com/tag/UCD',  # UCD
                        # 'https://book.douban.com/tag/java',  # java
                        # 'https://book.douban.com/tag/python',  # python
                        # 'https://book.douban.com/tag/c++',  # c++
                        # 'https://book.douban.com/tag/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%8',  # 人工智能
                        # 'https://book.douban.com/tag/%E7%A7%91%E6%99%AE',  # 科普
                        'https://book.douban.com/tag/%E8%AE%A1%E7%AE%97%E6%9C%BA', #计算机

        ]

        # cook = "{'bid': 'qnrg-Om6HSo', 'gr_user_id': 'adbd942a-6e95-40c6-be0f-d2fc0114e81b', '_vwo_uuid_v2': 'DEF3C8C1A63D796DBFDC8E1F0895BDADB|026bb6ddc7dfa0977cfd98309e6412c0', 'll': '118172', 'Hm_lvt_6e5dcf7c287704f738c7febc2283cf0c': '1555329797,1555424331,1555431024,1555513908', 'douban-fav-remind': '1', '_ga': 'GA1.2.113169978.1553871196', 'ct': 'y', '__utmc': '81379588', 'viewed': '26929955_5375620_26582822_27030507_1767945_24738302_26838557_27168433_1119944_26834485', 'dbcl2': '146494461:ssWrzbB2DTI', 'ck': 'Uu4j', '_pk_ref.100001.3ac3': '%5B%22%22%2C%22%22%2C1556510481%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fredir%3Dhttps%253A%252F%252Fbook.douban.com%252Ftag%252F%2525E7%2525AE%252597%2525E6%2525B3%252595%253Fstart%253D420%2526type%253DT%22%5D', '_pk_id.100001.3ac3': '7cd6ce805e596b91.1553871196.32.1556510481.1556497709.', '_pk_ses.100001.3ac3': '*', '__utma': '81379588.468017531.1553871196.1556497515.1556510481.31', '__utmz': '81379588.1556510481.31.6.utmcsr', '__utmt_douban': '1', '__utmb': '81379588.1.10.1556510481', '__utmt': '1', 'push_doumail_num': '0', 'push_noty_num': '3'}"

        for url in start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = "https://book.douban.com/tag/"
        isFirst = re.findall('start=(\d*)&', response.url)
        if isFirst:
            pass
        else:
            try:
                related = response.xpath('//div[@class="tags-list"]/a/@href').extract()
            except:
                related = None
            for rel in related:
                next_tag = parse.quote(rel)
                next_tag = 'https://book.douban.com' + next_tag
                with open("tag.txt") as f:
                    url_list = f.read()
                if next_tag not in url_list:
                    with open("tag.txt", "a") as f:
                        f.write(next_tag + '----')
                    yield Request(next_tag)


            # print(related)
        try:
            result = (response.url.split('ag')[0]) in urls # 判断是否为列表页
        except:
            result = False
        ret = 'doings'
        item = BooksItem()

        # wait = round(random.uniform(0, 1), 2)
        # time.sleep(wait)
        # print(wait)


        if result:

            # 详情页
            count = 0
            for href in response.xpath('//li[@class="subject-item"]/div[@class="info"]//h2//a/@href').extract():
                count += 1
                with open("url.txt") as f:
                    url_list = f.read()
                if href not in url_list:
                    with open("url.txt", "a") as f:
                        f.write(href + '----')
                    print(href)
                    yield Request(href)

            print(response.url)
            if count == 0:
                print('---------------------------------------------------------------')


            # yield下一页链接
            try:
                next = response.xpath('//span[@class="next"]/link/@href').extract_first()
            except:
                next = None
            if next:
                next_url = 'https://book.douban.com' + next
                yield Request(next_url)

        # elif ret in response.url:
        #     item['url'] = response.url.split('/d',1)[0]
        #     try:
        #         item['read'] = response.xpath('//*[@id="collections_bar"]/span/a/text()').extract()[0]
        #         item['read'] = re.findall(r'\d*', item['read'])[0]
        #     except:
        #         print("No find read!")
        #         item['read'] = 0
        #
        #     try:
        #         item['read_want'] = response.xpath('//*[@id="wishes_bar"]/span/a/text()').extract()[0]
        #         item['read_want'] = re.findall(r'\d*', item['read_want'])[0]
        #
        #     except:
        #         print("No find read_want!")
        #         item['read_want'] = 0
        #
        #     try:
        #         item['reading'] = response.xpath('//*[@id="doings_bar"]/span/text()').extract()[0]
        #         item['reading'] = re.findall(r'\d*', item['reading'])[0]
        #     except:
        #         print("No find reading!")
        #         item['reading'] = 0
        #     try:
        #         base_info = response.xpath('//div[@class="indent"]').extract()[0].replace('\n', '').replace(' ', '')
        #         item['ISBN'] = re.findall(r'isbn:</span>(\d*)<br>', base_info)[0]
        #     except:
        #         print('No find ISBN!')
        #         item['ISBN'] = 0
        #     try:
        #         item['author'] = re.findall(r"作者:(.*?)</span>", base_info, re.S)[0]
        #     except:
        #         print('No find 作者!')
        #         item['author'] = 0
        #     try:
        #         item['title'] = re.findall(r'书名:</span>(.*?)<br>', base_info)[0]
        #     except:
        #         item['title'] = 0
        #     try:
        #         item['press'] = re.findall(r'出版社:</span>(.*?)<br>', base_info)[0]
        #     except:
        #         item['press'] = 0
        #     try:
        #         item['trans'] = re.findall(r'译者:(.*?)</span>', base_info)[0]
        #     except:
        #         item['trans'] = 0
        #     try:
        #         date = re.findall(r'出版年:</span>(.*?)<br>', base_info)[0]
        #         item['publish_date'] = re.findall(r'\d*-\d+', date)[0]
        #     except:
        #         item['publish_date'] = 0
        #
        #     try:
        #         item['price'] = re.findall(r'定价:</span>:(\d*.\d*)<br>', base_info)[0]
        #     except:
        #         item['price'] = 0
        #
        #     try:
        #         item['score'] = response.xpath('//*[@id="content"]/div/div[1]/div[1]/div[1]/p/strong/text()').extract()[0]
        #     except:
        #         item['score'] = 0
        #     try:
        #         number = response.xpath('//*[@id="content"]/div/div[1]/h2/span/text()').extract()[0]
        #         item['number'] = re.findall(r'(\d*)', number)[0]
        #     except:
        #         item['number'] = 0
        #     try:
        #         item['image'] = response.xpath('//*[@id="content"]/div/div[2]/div[2]/a/img/@src').extract()[0]
        #     except:
        #         item['image'] = 0
        #
        #     try:
        #         distr = response.xpath('//div[@class="rating_detail_star"]').extract()[0].replace('\n', '').replace(' ', '')
        #         part = re.compile("(\d*.\d*)%")
        #         item['one'] = part.findall(distr)[4]
        #         item['two'] = part.findall(distr)[3]
        #         item['three'] = part.findall(distr)[2]
        #         item['four'] = part.findall(distr)[1]
        #         item['five'] = part.findall(distr)[0]
        #     except:
        #         print('can not find distr')
        #         item['one'] = 0
        #         item['two'] = 0
        #         item['three'] = 0
        #         item['four'] = 0
        #         item['five'] = 0
        #     try:
        #         item['reading_date'] = response.xpath('//div[@class="sub_ins"]//tr/td//p[@class="pl"]/span[1]/text()').extract()[0]
        #     except:
        #         item['reading_date'] = 0
        #
        #
        #
        #     postitem = dict(item)
        #     tes.insert(postitem)


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

            # 基本信息
            try:
                base_info = response.xpath('//div[@id="info"]').extract()[0].replace('\n', '').replace(' ', '')
                item['info'] = base_info
            except:
                item['info'] = None

            try:
                author = re.findall(r"作者(.*?)</a>", base_info, re.S)[0]
                part = re.compile(r'">(.*)')
                item['author'] = part.findall(author)[0]
            except:
                print("No find author!")
                item['author'] = 0

            try:
                part = re.findall(r"译者</span>(.*?)</a>", base_info, re.S)[0]
                ret = re.compile(r'">(.*)')
                item['trans'] = ret.findall(part)[0]
            except:
                print("trans find error!")
                item['trans'] = 0


            try:
                press = re.findall(r'出版社(.*?)<br>', base_info)[0]
                part = re.compile(r'</span>(.*)')
                press = part.findall(press)[0]
                item['press'] = press
            except:
                print("No find press!")
                item['press'] = 0
            try:
                item['price'] = re.findall(r'定价:</span>(\d*.\d*)', base_info)[0]
            except:
                item['price'] = 0

            try:
                item['pages'] = re.findall(r'页数:</span>(\d*)<br>', base_info)[0]
            except:
                item['pages'] = None

            try:
                ret = re.findall(r'出版年(.*?)<br>', base_info)[0]
                ret = re.findall(r'\d*-\d+', ret)[0]
                item['publish_date'] = ret
            except:
                print("No find date!")
                item['publish_date'] = 0
            try:
                item['ISBN'] = re.findall(r'ISBN:</span>(\d*)', base_info)[0]
            except:
                item['ISBN'] = None

            try:
                reads = response.text
            except:
                pass
            try:
                item['reading'] = re.findall(r'>(\d*)人在读', reads)[0]
            except:
                item['reading'] = 0
            try:
                item['read_want'] = re.findall(r'>(\d*)人想读', reads)[0]
            except:
                item['read_want'] = 0
            try:
                item['read'] = re.findall(r'>(\d*)人读过', reads)[0]
            except:
                item['read'] = 0
            # try:
            #     read = response.xpath('//div[@id="collector"]/p/a/text()').extract()
            #     item['reading'] = re.findall(r'(\d*)人在读', read)[0]
            # except:
            #     # print("reading find error!")
            #     item['reading'] = 0
            #
            # try:
            #     item['read'] = re.findall(r'(\d*)人读过', read)[0]
            # except:
            #     # print("read find error!")
            #     item['read'] = 0
            #
            # try:
            #     item['read_want'] = re.findall(r'(\d*)人想读', read)[0]
            # except:
            #     # print('read_want find error!')
            #     item['read_want'] = 0

            try:
                item['label']= response.xpath('//div[@id="db-tags-section"] /div[@class="indent"]/span/a/text()').extract()
            except:
                print("No label!")
                item['label'] = 0
            try:
                item['image'] = response.xpath('//*[@id="mainpic"]/a/img/@src').extract()[0]
            except:
                item['image'] = None

            try:
                item['short'] = response.xpath('//*[@id="comments"]//p[@class="comment-content"]/span/text()').extract()
            except:
                item['short'] = 0
            try:
                ret = response.xpath('//div[@id="buyinfo-ebook"]//li//text()').extract()
                item['price_d'] = re.findall(r'(\d*.\d*)', ret)[0]
            except:
                item['price_d'] = 0

            try:
                ret = response.xpath('//div[@class="mod-hd"]/h2/span/a/text()').extract()[0]
                item['short_number'] = re.findall(r'(\d+)', ret)[0]
            except:
                item['short_number'] = 0

            try:
                ret = response.xpath('//section[@class="reviews mod book-content"]//h2/span/a/text()').extract()[0]
                item['book_number'] = re.findall(r'(\d+)', ret)[0]
            except:
                item['book_number'] = 0

            try:
                ret = response.xpath('//div[@class="ugc-mod reading-notes"]//span/a/span/text()').extract()[0]
                item['note_number'] = ret
            except:
                item['note_number'] = 0

            try:
                distr = response.xpath('//div[@class="rating_wrap clearbox"]').extract()[0].replace('\n', '').replace(' ', '')
                part = re.compile("(\d*.\d*)%")
                item['one'] = part.findall(distr)[4]
                item['two'] = part.findall(distr)[3]
                item['three'] = part.findall(distr)[2]
                item['four'] = part.findall(distr)[1]
                item['five'] = part.findall(distr)[0]
            except:
                print('can not find distr')
                item['one'] = 0
                item['two'] = 0
                item['three'] = 0
                item['four'] = 0
                item['five'] = 0

            # 想看 详情页
            # yield Request(response.url + 'doings')

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
        #     print(item)

            postitem = dict(item)
            all.insert(postitem)
