# -*- coding: utf-8 -*-
import scrapy
from MoneyReport.items import MoneyreportItem
import re
import json


class ReportSpiderSpider(scrapy.Spider):
    name = 'report_spider'
    allowed_domains = ['datainterface.eastmoney.com']
    pagenum = 1
    urls = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&js=var%20zPmnaRZr={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=50&mkt=0&stat=0&cmd=4&code=&rt=51841034&p='
    start_urls = [ urls + str(pagenum) ]

    def parse(self, response):
        # print response.text
        # 转换为符合的格式
        txt = response.text
        # 取出script中间的内容
        script_data = re.search("{\"data\":\[([\s\S]*)(],\"page)", txt)
        print script_data.group(1)
        if script_data:
            tmp_data = script_data.group(1)
            # 将内容分行
            lines = tmp_data.replace('},{', '}\n{')
            # 将内容转换为json格式
            jsondict = []
            for line in lines.splitlines():
                # print line
                tojson = json.loads(line)
                jsondict.append(tojson)
            report_item = MoneyreportItem()
            for jsonline in jsondict:
                report_item['num'] = jsonline['change']
                report_item['date'] = jsonline['datetime']
                report_item['code'] = jsonline['secuFullCode']
                report_item['name'] = jsonline['secuName']
                report_item['title'] = jsonline['title']
                report_item['rating'] = jsonline['rate']
                report_item['ratchange'] = jsonline['change']
                report_item['agency'] = jsonline['insName']
                report_item['eight_forreturn'] = jsonline['sys'][0]
                report_item['eight_forPE'] = jsonline['syls'][0]
                report_item['nine_forreturn'] = jsonline['sys'][1]
                report_item['nine_forPE'] = jsonline['syls'][1]
                yield report_item
        # 解析下一页规则,页数增加1
        # 获取总页数
        totalnum = re.search("page\":\"([\d]*)\",\"update", txt).group(1)
        if self.pagenum < int(totalnum)+1:
            self.pagenum += 1
            print '爬取页数：%d'%self.pagenum
            yield scrapy.Request(self.urls + str(self.pagenum), callback=self.parse)
        print '处理结束'



