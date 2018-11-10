import scrapy

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
        
        
        for item in zip(titulo,autor,resumen,editor,year):
            scraped_info={
                 'titulo' : item[0],
                 'autor' : item[1],
                 'resumen'  : item[2],
                 'editor': item[3],
                 'year' : item[4]
            }

        
            yield scraped_info
		

