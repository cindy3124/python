# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoneyreportItem(scrapy.Item):
    # define the fields for your item here like:
    # 序号
    num = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # 代码
    code = scrapy.Field()
    # 名称
    name = scrapy.Field()
    # 研报
    title = scrapy.Field()
    # 原文评级
    rating = scrapy.Field()
    # 评级变动
    ratchange = scrapy.Field()
    # 机构
    agency = scrapy.Field()
    # 2018预测收益
    eight_forreturn = scrapy.Field()
    # 2018预测市盈率
    eight_forPE = scrapy.Field()
    # 2019预测收益
    nine_forreturn = scrapy.Field()
    # 2019预测市盈率
    nine_forPE = scrapy.Field()