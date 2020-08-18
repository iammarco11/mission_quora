import urllib
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.quora.com/What-are-the-pro-tips-for-GSOC"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

indexhtml = str(soup.prettify())
f = open("index.html", "w")
f.write(indexhtml)
f.close()

result = soup.find_all("script",{"type": "application/ld+json"})

g = open("quora.json","w")
g.write(str(result))
g.close()
