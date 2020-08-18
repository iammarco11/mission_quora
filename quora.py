import urllib
import requests
from bs4 import BeautifulSoup
import json

url = input("Input the Discussion URL of Quora:")

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

indexhtml = str(soup.prettify())
f = open("index.html", "w")
f.write(indexhtml)
f.close()

result = soup.find_all("script",{"type": "application/ld+json"})

g = open("quora.html","w")
g.write(str(result))
g.close()
