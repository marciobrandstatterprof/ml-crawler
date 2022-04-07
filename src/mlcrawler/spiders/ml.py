import scrapy
from ..items import MlcrawlerItem


class MlSpider(scrapy.Spider):
    name = 'ml'
    start_urls = ['https://www.mercadolivre.com.br/ofertas?page=1']

    def parse(self, response, **kwargs):
        url = response.xpath('//a[contains(text(),"Alimentos e Bebidas")]/@href').get()
        yield scrapy.Request(url=url, callback=self.parse_bebidas)
        
        
    def parse_bebidas(self, response):
        url = response.xpath(
            '//ol[@class="list"]/li/a[contains(text(),"Bebidas")]/@href').get()
        yield scrapy.Request(url=url, callback=self.parse_itens)
    
        
    def parse_itens(self, response, **kwargs):
        book = MlcrawlerItem()
        for i in response.xpath('//li[@class="promotion-item min"]'):            
            book['title'] = i.xpath('.//p[@class="promotion-item__title"]/text()').get()
            book['seller'] = i.xpath('.//p[@class="promotion-item__seller"]/text()').get()
            book['price'] = i.xpath(
                './/span[@class="promotion-item__price"]//text()').getall()
            book['discount'] = i.xpath(
                './/span[@class="promotion-item__discount"]//text()').getall()
            book['old_price'] = i.xpath(
                './/span[@class="promotion-item__oldprice"]//text()').getall()
            book['shipping'] = i.xpath(
                './/span[@class="promotion-item__shipping"]//text()').getall()
            book['link'] = i.xpath('./a/@href').get()

            yield book

        next_page = response.xpath(
            '//li[@class="andes-pagination__button andes-pagination__button--next"]/a[@class="andes-pagination__link"][contains(@title, "Próxima")]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse_itens)
