'''
* Ejercicio 2.0 realizando un request, utilizando la librería requests
* @version 1.0
* autor datascientistperu@gmail.com
* 1er Workshop de WebCrawler & Web Scraping, noviembre 2018
* Universidad Ricardo Palma - (Lima - Perú)
'''


import requests

url='http://www.sunat.gob.pe/cl-at-ittipcam/tcS01Alias'

r=requests.get(url)

print(r.text)

