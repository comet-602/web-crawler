import requests
from bs4 import BeautifulSoup

html = 'http://www.pythonscraping.com/pages/warandpeace.html'
res = requests.get(html)
bs = BeautifulSoup(res.text, "html.parser")

nameList = bs.findAll('span', {'class': 'green'})
for i,name in enumerate(nameList):
    print(i,name.text)
print(len(nameList))
print('==================================')
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print([title for title in titles])
print('==================================')
nameList = bs.find_all(text='the prince')
print(nameList)
print(len(nameList))


