from scrapy.crawler import CrawlerProcess
from spiders.scrapy_settings import get_tge_settings
from spiders.tge_spider import TGeSpider

if __name__ == '__main__':
    process = CrawlerProcess(settings=get_tge_settings())
    process.crawl(TGeSpider)
    process.start()

