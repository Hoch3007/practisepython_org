##### practicepython.org: Exercise 19

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.mirror.co.uk/sport/tennis/andy-murray-crashes-out-brisbane-13802534")
r_html = r.text
soup = BeautifulSoup(r_html)

text = soup.select("div.article-body > p")

full_text = []

for i in text:    
    full_text.append(i.string)
    
print " ".join(full_text)

fertiger_text = " ".join(full_text)

##### practicepython.org: Exercise 21

filename = raw_input("Wie soll die Datei benannt sein? ")

with open(filename+".txt", "w") as open_file:
    open_file.write(fertiger_text.encode('utf-8'))

# Wichtig: Die Zeichenkodierung ist sonst ASCII und da sind einige Zeichen nicht drin,
# am besten in einem Schritt auf UTF-8 umstellen.

##### practicepython.org: Exercise 22

 with open('andy_murry_brisbane.txt', 'r') as open_file:
    all_text = open_file.read()

all_text

names = {'Andy': 0, 'Murray': 0, 'Daniil': 0, 'Medvedev':0}

text = all_text.replace('.', ' ')

text = text.replace(',', ' ')

text= text.split()

for i in text:
    #print i
    
    if i in names.keys():
        print i
        names[i] +=1
        print names[i]

names
