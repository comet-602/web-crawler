import requests,os
from bs4 import BeautifulSoup

if not os.path.exists('./pttgo'):
    os.mkdir('./pttgo')
cookies={'over18':'1'}

headers={'User+Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

url='https://www.ptt.cc/bbs/Gossiping/index38895.html'
re = requests.get(url, headers=headers,cookies=cookies)
sou = BeautifulSoup(re.text, 'html.parser')
cont=sou.select('div.title')
htm='https://www.ptt.cc'
for c in cont:
    try:
        title=c.a.text
        print(title)
        html=htm+c.a['href']
        print(html)
        with open('./pttgo/%s.txt' % title.replace('?','').replace(':',''), 'w', encoding='utf-8') as f:
            f.write('content')
    except AttributeError as p:
        print(p)


