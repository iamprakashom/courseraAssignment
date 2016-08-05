from urllib.request import urlopen
from bs4 import BeautifulSoup

urldata = urlopen('http://python-data.dr-chuck.net/comments_42.html')
soupdata = BeautifulSoup(urldata.read())

tag = soupdata.find_all("span", {"class": "comments"})
sum = 0
# Adding all the numerical value given on above url
for tgs in tag:
    sum += int(tgs.contents[0])

print(sum)
