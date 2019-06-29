from scrapy import cmdline

# cmdline.execute('scrapy crawl report_spider'.split())

cmdline.execute('scrapy crawl report_spider -o MoneyReport_2year.csv'.split())