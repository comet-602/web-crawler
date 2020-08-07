import requests,os
from bs4 import BeautifulSoup

if not os.path.exists('./pttgo'):
    os.mkdir('./pttgo')
cookies={'over18':'1'}

headers={'User+Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url='https://www.ptt.cc/bbs/Gossiping/M.1588288876.A.14C.html'

res = requests.get(url, headers=headers,cookies=cookies)
soup = BeautifulSoup(res.text, 'html.parser')
content = soup.select('div#main-content')[0].text.split('--')[0]
#print(content)
content+='=======================================================\n'
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

title=soup.select('div.article-metaline')
if title==[]:
    content += '作者:None\n'
    content += '標題:None\n'
    content += '時間:None\n'
    print(content)
else:
    info = soup.select('div[id="main-content"] div[class="article-metaline"]')[0].text[2:]
    info1 = soup.select('div[id="main-content"] div[class="article-metaline"]')[1].text[2:]
    info2 = soup.select('div[id="main-content"] div[class="article-metaline"]')[2].text[2:]
    content += '作者:%s\n' % info
    content += '標題:%s\n' % info1
    content += '時間:%s\n' % info2
    print(content)

#
# # save article
# with open('./pttgo/%s.txt' % info1.replace('"','-').replace('/','-').replace(':','-').replace('?',''), 'w', encoding='utf-8') as f:
#     f.write(content)

