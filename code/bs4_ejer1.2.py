'''
* Ejercicio 1.2, realizando un parser, utilizando la librería BeautifulSoup y request
* @version 1.2
* autor datascientistperu@gmail.com
* 1er Workshop de WebCrawler & Web Scraping, noviembre 2018
* Universidad Ricardo Palma - (Lima - Perú)
'''

from bs4 import BeautifulSoup
import requests

url='http://v-beta.urp.edu.pe/posgrado/maestrias/ciencia-de-los-datos/'

r=requests.get(url)

html_soup= BeautifulSoup(r.text, 'html.parser')



div= html_soup.find(id='tab1488934671815_6')

div_tables=div.find_all(class_='col-sm-10') #almacenamos todos los div de la clase


for  indice_div  in div_tables:
	profesor = indice_div.b.text
	descripcion = indice_div.div.text
	print("docente : " ,profesor)
	print("experiencia : ", descripcion,'\n')





