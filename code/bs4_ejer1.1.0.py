'''
* Ejercicio 1.1.0, realizando un parser, utilizando la librería BeautifulSoup y request
* @version 1.1.0
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

div_tables=div.find_all(class_='col-sm-10')



print("docente : ",div_tables[0].b.text)
print("experiencia : ",div_tables[0].div.text,'\n')

print("docente : ",div_tables[1].b.text)
print("experiencia : ",div_tables[1].div.text,'\n')

print("docente : ",div_tables[2].b.text)
print("experiencia : ",div_tables[2].div.text,'\n')

print("docente : ",div_tables[3].b.text)
print("experiencia : ",div_tables[3].div.text,'\n')

b_tables=div_tables[4].find_all('b') #se implemento este arreglos de <b> por qué no sigue una diseño estándar
print("docente : ",b_tables[1].text) # se hace referencia al indice = 1 es donde se encuentra elemento 
print("experiencia : ",div_tables[4].div.text,'\n')

print("docente : ",div_tables[5].b.text)
print("experiencia : ",div_tables[5].div.text,'\n')

print("docente : ",div_tables[6].b.text)
print("experiencia : ",div_tables[6].div.text,'\n')

print("docente : ",div_tables[7].b.text)
print("experiencia : ",div_tables[7].div.text,'\n')

print("docente : ",div_tables[8].b.text)
print("experiencia : ",div_tables[8].div.text,'\n')

