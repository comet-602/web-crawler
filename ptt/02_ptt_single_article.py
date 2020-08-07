import requests,os
from bs4 import BeautifulSoup

if not os.path.exists('./pttgo'):
    os.mkdir('./pttgo')
cookies={'over18':'1'}

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url='https://www.ptt.cc/bbs/Gossiping/M.1590837116.A.6BC.html'

res = requests.get(url, headers=headers,cookies=cookies)
soup = BeautifulSoup(res.text, 'html.parser')
content = soup.select('div#main-content')[0].text.split('--')[0]
#print(content)
#content+='=======================================================\n'
# get the good article
good=0
bad=0
no=0
push_article = soup.select('div.push')
for push in push_article:
    if '推' in push.text:
        good+=1
    elif '噓' in push.text:
        bad+=1
    else:
        no+=1
content+='推的量:%d\n' %good
content+='噓的量:%d\n' %bad
content+='無表達:%d\n' %no
#print(content)
detail_info=[]
title=soup.select('div.article-metaline')
if title==[]:
    content += '作者:None\n'
    content += '標題:None\n'
    content += '時間:None\n'
    print(content)
#print(title)
else:
    for i, info in enumerate(title):
        detail_info.append(info.text)
    content += '作者:%s\n' % detail_info[0][2:]
    content += '標題:%s\n' % detail_info[1][2:]
    content += '時間:%s\n' % detail_info[2][2:]
    print(content)



# save article
# with open('./pttgo/%s.txt' % detail_info[1][2:].replace('"','-').replace('/','-').replace(':','-').replace('?',''), 'w', encoding='utf-8') as f:
#     f.write(content)





