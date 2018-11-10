'''
* Ejercicio 1 realizando un request, utilizando la librería requests
* @version 1.0
* autor datascientistperu@gmail.com
* 1er Workshop de WebCrawler & Web Scraping, noviembre 2018
* Universidad Ricardo Palma - (Lima - Perú)
'''

from bs4 import BeautifulSoup
import requests

url='https://www.youtube.com/watch?v=xTYCVBIGWrc'

r=requests.get(url)

#print(r.text)

html_soup= BeautifulSoup(r.text, 'html.parser')

print(html_soup)


#div= html_soup.find('ytd-comments',attrs={'class':'style-scope ytd-watch-flexy'})
#print(div)


