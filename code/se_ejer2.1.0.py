'''
* Ejercicio 2.1 realizando un request, utilizando la librería requests, selenium
* @version 1.1
* autor datascientistperu@gmail.com
* 1er Workshop de WebCrawler & Web Scraping, noviembre 2018
* Universidad Ricardo Palma - (Lima - Perú)
'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select



driver = webdriver.Firefox()
url = 'http://www.sunat.gob.pe/cl-at-ittipcam/tcS01Alias'

driver.get(url)


select_mes = Select(driver.find_element_by_xpath("//select[@name='mes']"))
select_mes.select_by_index(10)


select_anho = Select(driver.find_element_by_xpath("//select[@name='anho']"))

#select_anho.select_by_index(2)
select_anho.select_by_value('2018')



driver.find_element_by_xpath("//input[@value='Consultar']").click()




driver.close

