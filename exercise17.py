##### practicepython.org: Exercise 17

import requests
from bs4 import BeautifulSoup

#url = "https://wiki.selfhtml.org/wiki/HTML/Regeln"
url = "https://www.mirror.co.uk/"

r = requests.get(url)
r_html = r.text

## Probleme mit BeautifulSoup, gelöst durch Neuinstallation auf dem Server mit
## https://stackoverflow.com/questions/40856104/importerror-cannot-import-name-htmlawareentitysubstitution

soup = BeautifulSoup(r_html)

type(soup)

headlines = soup.find_all("a","headline")

titles = []
for i in headlines:
    print i
    titles.append(i.string)    

titles
