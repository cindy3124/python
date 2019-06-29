# -*- coding: utf-8 -*-
import scrapy, sys
from Tencent.items import TencentItem


class TencentpostionSpider(scrapy.Spider):
    '''
    功能：爬取腾讯社招信息
    '''
    # 爬虫名
    name = 'tencentPostion'
    # 爬虫作用范围，允许的域名
    # allowed_domains = ['tencent.com']
    allowed_domains = ['movie.douban.com']

    # url = "http://hr.tencent.com/position.php?&start="
    url = "https://movie.douban.com/top250"
    # offset = 0
    # 入口url，扔到调度器里面
    # start_urls = [ url + str(offset) ]
    start_urls = [url]
    print '打印的URL是:'
    print start_urls

    # 默认解析方法
    def parse(self, response):
        print response.text
        print '打印response.text结束'
        # for each in response.xpath("//tr[@class='event']|tr[@class='odd']"):
        print '开始打印符合的xpath'
        # 循环电影的条目
        for each in response.xpath("//div[@class='article']//ol[@class='grid_view']/li"):
            print each
            # item文件导进来
            douban_item = TencentItem()
            # 写详细的xpath，进行数据的解析
            douban_item['serial_number'] = each.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = each.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            print douban_item
            # 将需要的数据传到管道中，否则pipelines接收不到数据
            yield douban_item
        # 解析下一页规则，取后一页的xpath
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link, callback=self.parse)
            '''
            # 初始化模型对象
            item = TencentItem()
            # 职位名称
            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item

        if self.offset < 100:
            self.offset += 10

        # 每次处理完一页的数据之后，重新发送下一页的页面请求
        # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
'''


