# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):

    # 书名
    title = scrapy.Field()

    # 作者
    author = scrapy.Field()

    # 出版社
    press = scrapy.Field()

    # 译者
    trans = scrapy.Field()

    # 出版年
    publish_date = scrapy.Field()

    # 页数
    # pages = scrapy.Field()

    # 定价
    price = scrapy.Field()

    # 电商价
    price_d = scrapy.Field()

    # 标签
    label = scrapy.Field()

    # ISBN
    ISBN = scrapy.Field()

    # 读过的人
    read = scrapy.Field()

    # 想读的人
    read_want = scrapy.Field()

    # 在读的人
    reading = scrapy.Field()

    # 评分
    score = scrapy.Field()

    # 评分人数
    number = scrapy.Field()

    # 图书链接
    url = scrapy.Field()

    # 作者简介
    # author_s = scrapy.Field()

    # 内容简介
    # summary = scrapy.Field()

    # 读过、想读、在读
    # read_box = scrapy.Field()

    # 图片链接
    image = scrapy.Field()

    # 一星
    one = scrapy.Field()

    # 二星
    two = scrapy.Field()

    # 三星
    three = scrapy.Field()

    # 四星
    four = scrapy.Field()

    # 五星
    five = scrapy.Field()

    # 短评
    short = scrapy.Field()

    # 短评数量
    short_number = scrapy.Field()

    # 书评数量
    book_number = scrapy.Field()

    # 笔记数量
    note_number = scrapy.Field()

    # 在读日期
    reading_date = scrapy.Field()

    # 读过日期
    read_date = scrapy.Field()

    # 想读日期
    readw_date = scrapy.Field()


