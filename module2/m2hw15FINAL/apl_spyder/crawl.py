from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

# myspd1 Is a crawl name
process.crawl('rozetka')
process.crawl('mta')

process.start()