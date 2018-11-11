'''
* Ejercicio 2 realizando un request, utilizando la librería requests
* @version 1.0
* autor datascientistperu@gmail.com
* 1er Workshop de WebCrawler & Web Scraping, noviembre 2018
* Universidad Ricardo Palma - (Lima - Perú)
'''

from selenium import webdriver
import requests

driver = webdriver.Firefox()

url = 'http://www.sunat.gob.pe/cl-at-ittipcam/tcS01Alias'

driver.get(url)

driver.close

