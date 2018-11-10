

from bs4 import BeautifulSoup
import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://v-beta.urp.edu.pe/posgrado/maestrias/ciencia-de-los-datos/')


#url='http://v-beta.urp.edu.pe/posgrado/maestrias/ciencia-de-los-datos/'
print(r.data)

