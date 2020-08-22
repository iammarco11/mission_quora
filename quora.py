import urllib
import requests
from bs4 import BeautifulSoup
import json

import re

def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext


def interact_json(json_obj):
	with open("quora.json", "w+") as f:
		f.write(json.dumps(json_obj, indent=4, sort_keys=True))

	with open("quora.json") as json_file:
		data = json.load(json_file)

	answers = data[0]['mainEntity']['suggestedAnswer']
	
	for i in range(0, len(answers)):
		print(answers[i]['author']['url'])
		print("\n")
		print(answers[i]['text'])
		print("\n")

url = input("Input the Discussion URL of Quora:")

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

indexhtml = str(soup.prettify())
f = open("index.html", "w")
f.write(indexhtml)
f.close()

result = soup("script",{"type": "application/ld+json"})
result = cleanhtml(str(result))

json_object = json.loads(str(result))

interact_json(json_object)
