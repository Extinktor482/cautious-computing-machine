from urllib.request import urlopen
from bs4 import BeautifulSoup
link = "https://www.heise.de/thema/https"
page = urlopen(link)
soup = BeautifulSoup(page, "lxml")
tags = soup('a')
for tag in tags:
    chk = tag.get('title', None)
    chk = str(chk)
    if chk == "Security-Funktion HSTS als Supercookie":
        h1 = chk
    if chk == "HTTPS entschlüsseln":
        h2 = chk
    if chk == "Verschlüsselung bei heise online":
        h3 = chk
h1 += " "
h1 += h2
h1 += " "
h1 += h3
from collections import Counter
counts = Counter(h1.lower().split())
print (counts)
for letter, count in counts.most_common(3):
    print (letter, count)