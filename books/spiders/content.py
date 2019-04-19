import scrapy
from books.items import BooksItem
from scrapy import Request
import re
import pymongo

client = pymongo.MongoClient('localhost',27017)
book = client['book']
all = book['all_data']

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
        urls = [      'https://book.douban.com/tag/%E4%BA%92%E8%81%94%E7%BD%91',  # 互联网

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

        item = BooksItem()

        if result:

            for href in response.xpath('//li[@class="subject-item"]/div[@class="info"]//h2//a/@href').extract():
                yield Request(href)
            print(response.url)
            # yield下一页链接
            # next = response.xpath('//span[@class="next"]/link/@href').extract_first()
            # if next != None:
            #     next_url = 'https://book.douban.com' + next
            #     yield Request(next_url)
        else:
            item['title'] = 'NULL'
            item['author'] = 'NULL'
            item['score'] = 'NULL'
            item['number'] = 'NULL'
            item['price'] = 'NULL'
            item['press'] = 'NULL'
            item['publish_date'] = 'NULL'
            item['pages'] = 'NULL'
            item['ISBN'] = 'NULL'
            item['label'] = 'NULL'
            item['read'] = 'NULL'
            item['read_want'] = 'NULL'
            item['reading'] = 'NULL'
            item['summary'] = 'NULL'
            item['author_s'] = 'NULL'

            item['url'] = response.url
            item['title'] = response.xpath('//h1/span/text()').extract()[0]
            score = response.xpath('//div[@id="interest_sectl"]//strong/text()').extract()[0].replace(' ','')
            if score =='':
                item['score']=0
            else:
                item['score']=score
            number = response.xpath('//div[@class="rating_sum"]//a//text()').extract()[0].replace('\n','')
            number = re.findall(r'\d*',number)[0]
            if number=='':
                item['number']=0
            else:
                item['number']=number

            infors = response.xpath('//div[@id="info"]').extract()[0].replace('\n','')

            author= re.findall(r"作者(.*?)</a>",infors,re.S)[0]
            part= re.compile(r'">(.*)')
            item['author']=part.findall(author)[0].replace(' ','')

            result = '出版社' in infors
            if result:
                press = re.findall(r'出版社(.*?)<br>',infors)[0]
                part=re.compile(r'</span>(.*)')
                press = part.findall(press)[0]
                if press=='':
                    item['press']=0
                else:
                    item['press']=press

            result = '出版年' in infors
            if result:
                publish_date=re.findall(r'出版年(.*?)<br>',infors)[0]
                pat=re.compile(r'</span>(.*)')
                date = pat.findall(publish_date)[0]
                date = re.findall(r'(\d\d\d\d)',date)[0]
                if date=='':
                    item['publish_date']=0
                else:
                    item['publish_date']=date
            # item['pages'] = re.match(r'.+页数:(.*?)定价', infors).group(1)
            # price = re.match(r'.+定价:(.*?)装帧', infors).group(1)
            # price = re.findall(r'(\d*\.\d*|\d*)',price)
            # for pair in price:
            #     if pair!='':
            #         item['price']=pair
            item['ISBN']=re.findall(r'ISBN:</span> (\d*)',infors)[0]
            read = response.xpath('//div[@class="indent"]').extract()[0].replace('\n','').replace(' ','')
            read_ = response.xpath('//*[@id="buyinfo-printed"]/ul/li[1]//text()').extract()
            print(read_[0].replace('\n','').replace(' ',''))
            print(item['ISBN'])
            print(response.url)
            # if read=='':
            #     item['read']=0
            # else:
            #     item['read'] = re.findall(r'\d*', read)[0]
            #     # item['read'] = re.findall(r'\d*',read)[0]
            #     # item['reading'] = re.findall(r'(\d*)人在读')[0]
            #     # item['read'] = re.findall(r'(\d*)人读过')[0]
            #     # item['read_want'] = re.findall(r'(\d*)人')[0]
            # read_want = response.xpath('//div[@class="indent"]/p[3]/a/text()').extract()[0]
            # if read_want==None:
            #     item['read_want']=0
            # else:
            #     item['read_want'] = re.findall(r'\d*', read_want)[0]
            #
            # reading = response.xpath('//div[@class="indent"]/p[1]/a/text()').extract()[0]
            # if reading == '':
            #     item['reading'] =0
            # else:
            #     item['reading'] = re.findall(r'\d*', reading)[0]

            label = response.xpath('//div[@id="db-tags-section"] /div[@class="indent"]/span/a/text()').extract()
            if label=='':
                item['label']=0
            else:
                item['label']=label

            # print(item)
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
            yield (item)
        # for items in all.find():
        #     yield items







