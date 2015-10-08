from bs4 import BeautifulSoup
import urllib2
import time
time.sleep(5)
actorSite = urllib2.urlopen('http://www.imdb.com/search/name?birth_monthday=01-28')
actorHTML =actorSite.read()
actorSite.close()
actorSoup = BeautifulSoup(actorHTML, 'lxml')
#print actorHTML

actorList = actorSoup.select('.name > a')
for actor in actorList:
    print actor.get_text()
    print 'www.imdb.com'+actor.get('href')
