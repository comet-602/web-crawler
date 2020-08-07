import requests
from bs4 import BeautifulSoup

html = 'http://www.pythonscraping.com/pages/page3.html'
res = requests.get(html)
bs = BeautifulSoup(res.text, "html.parser")

#只呼叫除本身的下一列
for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)