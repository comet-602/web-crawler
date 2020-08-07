import requests,os
from bs4 import BeautifulSoup

if not os.path.exists('./pttpi'):
    os.mkdir('./pttpi')
cookies={'over18':'1'}

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url='https://www.ptt.cc/bbs/Beauty/M.1590323835.A.C65.html'

res = requests.get(url, headers=headers,cookies=cookies)
soup = BeautifulSoup(res.text, 'html.parser')
img = soup.select('div#main-content a')
for i in img:
    print(i.text)


# save article
with open('./pttgo/%s.txt' % detail_info[1][2:].replace('"','-').replace('/','-').replace(':','-').replace('?',''), 'w', encoding='utf-8') as f:
   f.write(content)





