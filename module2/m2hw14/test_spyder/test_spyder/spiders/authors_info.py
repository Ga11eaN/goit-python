import scrapy


class AuthorsInfoSpider(scrapy.Spider):
    name = "authors_info"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            author_link = self.start_urls[0] + quote.xpath("span//a/@href").get()
            print(author_link)
            yield scrapy.Request(author_link, callback=self.parse_author)

    def parse_author(self, response):
        author_name = response.xpath(
            "/html//div[@class='author-details']/h3/text()"
        ).get()
        author_birth = response.xpath(
            "/html//span[@class='author-born-date']/text()"
        ).get()
        author_desc = response.xpath(
            "/html//div[@class='author-description']/text()"
        ).get()

        yield {"author": author_name, "birth_date": author_birth, "desc": author_desc}
