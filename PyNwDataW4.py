from urllib.request import urlopen
from bs4 import BeautifulSoup

# Change the given url if needed
urldata = urlopen('http://python-data.dr-chuck.net/comments_42.html')
soupdata = BeautifulSoup(urldata.read())

tag = soupdata.find_all("span", {"class": "comments"})
sum = 0
# Adding all the numerical value given on above url
for tgs in tag:
    sum += int(tgs.contents[0])


tagsA = soupdata.find_all('a')
for tg in tagsA:
    print ("TAG", tg)
    print("URL", tg.get('href', None))
    print('Contents:', tg.contents[0])
    print('Attrs', tg.attrs)
    print(tg)

print(sum)
