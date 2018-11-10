'''
* Ejercicio 1.2.2, realizando un parser ,aplicando limpiza al campo descripcion, preparando los datos en un json 
* se utilizo la librería BeautifulSoup y request
* @version 1.2.2
* autor datascientistperu@gmail.com
* 1er Workshop de WebCrawler & Web Scraping, noviembre 2018
* Universidad Ricardo Palma - (Lima - Perú)
'''

from bs4 import BeautifulSoup
import requests
import pprint

url='http://v-beta.urp.edu.pe/posgrado/maestrias/ciencia-de-los-datos/'

r=requests.get(url)

html_soup= BeautifulSoup(r.text, 'html.parser')



div= html_soup.find(id='tab1488934671815_6')

div_tables=div.find_all(class_='col-sm-10') #recuperamos todos los div de la clase

contador=0

for indice in div_tables:
	profesor = indice.b.text
	descripcion = indice.div.text

	if contador==4:
		b_tables = div_tables[contador].find_all('b')
		docente = b_tables[1].text.strip()
		experiencia = descripcion[len(b_tables[1].text):len(descripcion)].strip()
	
	else:
		docente = profesor.strip()
		experiencia = descripcion[len(profesor):len(descripcion)].strip()
	

	
	contador+=1

	dataJson={"docente":docente,"experiencia":experiencia} #datos preparados en un json
	pprint.pprint(dataJson)






