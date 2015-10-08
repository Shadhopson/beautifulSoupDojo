import urllib2
from bs4 import BeautifulSoup
import time

docURL = 'https://www.zocdoc.com/search/?dr_specialty=&address=10013&insurance_carrier=-1&refine_search=Find+a+Doctor'

url = urllib2.urlopen(docURL)
docHTML = url.read()
url.close()

docSoup = BeautifulSoup(docHTML, 'lxml')
docs = docSoup.select('a > .js-profile-link')
print docs
siteList=[]
for doc in docs:
    siteList.append(doc.get('href'))

for site in siteList:
    time.sleep(3)
    url = urllib2.urlopen(site)
    docHTML = url.read()
    url.close()
    docSoup = BeautifulSoup(docHTML, 'lxml')
    comments = docSoup.select('.comments')
    for comment in comments:
        print comment.get_text()


