from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('http://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')
pause = 0.01
for i in range(0,100):
   time.sleep(pause)
   htmlElem.send_keys(Keys.DOWN)
   time.sleep(pause)
   htmlElem.send_keys(Keys.LEFT)
   time.sleep(pause)
   htmlElem.send_keys(Keys.UP)
   htmlElem.send_keys(Keys.RIGHT)
