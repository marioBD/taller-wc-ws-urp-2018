'''
* Ejercicio 2.1 realizando un request, utilizando la librería requests
* @version 1.1
* autor datascientistperu@gmail.com
* 1er Workshop de WebCrawler & Web Scraping, noviembre 2018
* Universidad Ricardo Palma - (Lima - Perú)
'''

from selenium import webdriver
import time 

driver = webdriver.Firefox()

url = 'http://www.sunat.gob.pe/cl-at-ittipcam/tcS01Alias'

driver.get(url)

time.sleep(3)

driver.close

