import requests

from bs4 import BeautifulSoup

page = requests.get("https://zuehlke.com")
print("GET result: " + str(page.status_code))

soup = BeautifulSoup(page.content, 'html.parser')

text = list(soup.findall('p'))
for x in text:
	print(x)
