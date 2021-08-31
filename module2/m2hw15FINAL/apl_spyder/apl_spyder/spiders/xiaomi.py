import scrapy
from ..items import AplSpyderItem

class RozetkaSpider(scrapy.Spider):
    name = 'rozetka'
    start_urls = ['https://rozetka.com.ua/mobile-phones/c80003/preset=smartfon;producer=xiaomi/']

    def parse(self, response):
        items = AplSpyderItem()
        
        phones = response.css('.goods-tile__inner')
        
        for phone in phones:
            title = phone.css('.goods-tile__title').css('::text').extract()
            link = phone.css('.goods-tile__heading::attr(href)').extract()
            price = phone.css('.goods-tile__price-value').css('::text').extract()
     
            items['title'] = title
            items['link'] = link
            items['price'] = price
            
            yield items
        
        #next_link = response.xpath("//li[@class='has-dropdown has-dropdown-games']").get()
        
class MtaSpider(scrapy.Spider):
    name = 'mta'
    start_urls = ['https://mta.ua/telefoni-ta-smartfoni/manufacturers_xiaomi']
    
    def parse(self, response):
        items = AplSpyderItem()
        
        phones = response.css('.productBlock')
        
        for phone in phones:
            title = phone.css('.product__name').css('::text').extract()
            link = phone.css('.product__name::attr(href)').extract()
            price = phone.css('.product__price:nth-child(1)').css('::text').extract()
     
            items['title'] = title
            items['link'] = link
            items['price'] = price
            
            yield items
            