import scrapy
from ..items import TestSpyderItem


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        items = TestSpyderItem()

        for quote in response.xpath("/html//div[@class='quote']"):

            tag = quote.xpath("div[@class='tags']/a/text()").extract()
            author = quote.xpath("span/small/text()").extract()
            title = quote.xpath("span[@class='text']/text()").get()
            author_link = self.start_urls[0] + quote.xpath("span//a/@href").get()

            items["title"] = title
            items["author"] = author
            items["tag"] = tag
            items["author_link"] = author_link

            yield items
