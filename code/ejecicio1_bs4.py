from bs4 import BeautifulSoup
url='http://v-beta.urp.edu.pe/posgrado/maestrias/ciencia-de-los-datos/'
soup = BeautifulSoup(url)
print(soup.prettify())

