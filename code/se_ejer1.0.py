from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.keys import Keys
import time 

profile = FirefoxProfile()
profile.set_preference('browser.cache.disk.enable', False)
profile.set_preference('browser.cache.memory.enable', False)
profile.set_preference('browser.cache.offline.enable', False)
profile.set_preference('network.cookie.cookieBehavior', 2)

driver = webdriver.Firefox(firefox_profile=profile)


url ='http://duckduckgo.com/'

driver.get(url)

driver.delete_all_cookies()

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("web scraping")
elem.send_keys(Keys.RETURN)

time.sleep(3)

driver.close()
