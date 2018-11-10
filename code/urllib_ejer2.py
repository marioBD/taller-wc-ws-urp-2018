'''
* Ejercicio 2 realizando un request, utilizando la librería urlib3
* @version 1.0
* autor datascientistperu@gmail.com
* 1er Workshop de WebCrawler & Web Scraping, noviembre 2018
* Universidad Ricardo Palma - (Lima - Perú)
'''

import urllib3

http = urllib3.PoolManager()

url = 'http://v-beta.urp.edu.pe/posgrado/maestrias/ciencia-de-los-datos/'

r = http.request('GET', url)

print(r.data)

