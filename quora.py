import urllib
import requests
from bs4 import BeautifulSoup
import json

import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

url = input("Input the Discussion URL of Quora:")

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

indexhtml = str(soup.prettify())
f = open("index.html", "w")
f.write(indexhtml)
f.close()

result = soup("script",{"type": "application/ld+json"})
result = cleanhtml(str(result))
print(result)

g = open("quora.html","w")
g.write(str(result))
g.close()
