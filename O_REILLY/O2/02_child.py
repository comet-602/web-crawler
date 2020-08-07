import requests
from bs4 import BeautifulSoup

html = 'http://www.pythonscraping.com/pages/page3.html'
res = requests.get(html)
bs = BeautifulSoup(res.text, "html.parser")

for child in bs.find('table',{'id':'giftList'}).children:
    print(child)
print('============================================')
for child1 in soup.find('table',{'id':'giftList'}).descendants:
    print(child1)