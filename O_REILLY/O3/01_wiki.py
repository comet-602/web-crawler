import requests
from bs4 import BeautifulSoup
import re

html = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
res = requests.get(html)
bs = BeautifulSoup(res.text, "html.parser")

links=bs.select('div#bodyContent')[0].select('a[href^="/wiki"][href^="#"]')
print(len(links))
#:re.compile'^(/wiki/)((?!:).)*$'---("^#")
for link in links:
    if 'href' in link.attrs : #.attrs將link轉為字典
        print(link.attrs['href']) #取出字典href的值

