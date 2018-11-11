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

#//tbody//td[@class='H3']/strong
#//tbody//td[@class="tne10"]
#dia=driver.find_element_by_xpath("//tbody/tr[2]/td[@class='H3'][1]/strong")
#tipoc=driver.find_element_by_xpath("//tbody//td[@class='tne10'][2]")

i=0
for ite in range(4):
	i+=1
	dia=driver.find_element_by_xpath("//tbody/tr[2]/td[@class='H3']["+str(i)+"]/strong")
	print(dia.text)

	
i=0
for ite in range(7):
	i+=1
	tipoc=driver.find_element_by_xpath("//tbody/tr[2]/td[@class='tne10']["+str(i)+"]")
	print(tipoc.text)


driver.close

