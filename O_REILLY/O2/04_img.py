import requests
from bs4 import BeautifulSoup
import re

html = 'http://www.pythonscraping.com/pages/page3.html'
res = requests.get(html)
bs = BeautifulSoup(res.text, "html.parser")

images = bs.find_all('img')
for image in images:
    print(image['src'])

print('============================================')
#使用正規表示篩選
images = bs.find_all('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])