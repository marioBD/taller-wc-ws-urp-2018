'''
* Ejercicio 1, realizando un parser, utilizando la librería BeautifulSoup y request
* @version 1.1
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

div10=div.find_all(class_='col-sm-10')



print(div10[0].b.text)
print(div10[0].div.text,'\n')

print(div10[1].b.text)
print(div10[1].div.text,'\n')

print(div10[2].b.text)
print(div10[2].div.text,'\n')

print(div10[3].b.text)
print(div10[3].div.text, '\n')

print(div10[4].b.text)
print(div10[4].div.text, '\n')

print(div10[5].b.text)
print(div10[5].div.text, '\n')

print(div10[6].b.text)
print(div10[6].div.text, '\n')

print(div10[7].b.text)
print(div10[7].div.text, '\n')


print(div10[8].b.text)
print(div10[8].div.text, '\n')



