from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import pymysql

print("Hello World\n")

print ("\nBeautifulSoup Test")
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        #returning null break
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
        print("SUCCESS")
    except AttributeError as e:
        return None
    return title
#title = getTitle("http://www.pythonscraping.com/pages/page1.html")
title = getTitle("http://en.wikipedia.org/wiki/Kevin_Bacon")
if title==None:
    print("Title could not be found")
else:
    print(title)

html=urlopen("http://www.rottentomatoes.com/m/donnie_darko/")
bsObj=BeautifulSoup(html)

for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])

print("\nDatabase Connection Test")
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='jog#oHD/J0wg', db='mysql')

cur = conn.cursor()
cur.execute("use scraping")
cur.execute("select * from pages where id=1")
print(cur.fetchone())
cur.close()
conn.close()
