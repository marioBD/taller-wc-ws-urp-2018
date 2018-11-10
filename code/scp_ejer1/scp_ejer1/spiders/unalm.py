import scrapy
from scp_ejer1.items import ScpEjer1Item

class UNALMSpider(scrapy.Spider):
    name = 'unalm'
    start_urls = ['http://repositorio.lamolina.edu.pe/handle/UNALM/3']

    def parse(self, response):
        #pass
        #titulo=response.css('.post-header>h2').extract() 
        titulo=response.xpath("//ul[@class='ds-artifact-list']//li[contains(@class,'ds-artifact-item')]//div[@class='artifact-title']/a/text()").extract()
        autor = response.xpath("//ul[@class='ds-artifact-list']//li[contains(@class,'ds-artifact-item')]//div[@class='artifact-info']//span[1]/span/text()").extract()
        resumen = response.xpath("//ul[@class='ds-artifact-list']//li[contains(@class,'ds-artifact-item')]//div[@class='artifact-abstract']/text()").extract()
        editor = response.xpath("//ul[@class='ds-artifact-list']//li[contains(@class,'ds-artifact-item')]//div[@class='artifact-info']//span[@class='publisher']/text()").extract()
        year=response.xpath("//ul[@class='ds-artifact-list']//li[contains(@class,'ds-artifact-item')]//div[@class='artifact-info']//span[@class='date']/text()").extract()
        
        
        for a_item in zip(titulo,autor,resumen,editor,year):
        	item = ScpEjer1Item()
        	item['titulo'] = a_item[0]
        	item['autor'] = a_item[1]
        	item['resumen'] = a_item[2]
        	item['editor'] = a_item[3]
        	item['year'] = a_item[4]

        	yield item
		

