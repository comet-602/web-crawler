from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
links=bs.find('div', {'id':'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$'))
for link in links:
    if 'href' in link.attrs:  # .attrs將link轉為字典
        print(link.attrs['href'])  # 取出字典href的值