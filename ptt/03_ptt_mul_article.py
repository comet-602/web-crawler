import requests,os
from bs4 import BeautifulSoup

if not os.path.exists('./pttgo'):
    os.mkdir('./pttgo')
cookies={'over18':'1'}

headers={'User+Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

url='https://www.ptt.cc/bbs/Gossiping/index.html'
re = requests.get(url, headers=headers,cookies=cookies)
sou = BeautifulSoup(re.text, 'html.parser')
cont=sou.select('div.title')
#get the each article
for c in cont:
    try:
        # get the each article title
        title_list=c.a.text
        print(title_list)
        # get the each article link
        html='https://www.ptt.cc'+c.a['href']
        print(html)
        #link to the each article and get the content
        res = requests.get(html, headers=headers,cookies=cookies)
        soup = BeautifulSoup(res.text, 'html.parser')
        #get the article content
        content = soup.select('div#main-content')[0].text.split('--')[0]

        content += '===========================================\n'
        # get the  article other information
        good = 0
        bad = 0
        no = 0
        push_article = soup.select('div.push')
        for push in push_article:
            if '推' in push.text:
                good += 1
            elif '噓' in push.text:
                bad += 1
            else:
                no += 1
        content += '推的量:%d\n' % good
        content += '噓的量:%d\n' % bad
        content += '無表達:%d\n' % no
        content += '分數:%d\n' % (good-bad)

        title = soup.select('div.article-metaline')
        if title == []:
            content += '作者:None\n'
            content += '標題:None\n'
            content += '時間:None\n'
            print('作者:None\n標題:None\n時間:None')
        else:
            for i, info in enumerate(title):
                if i == 0:
                    author = info.text[2:]
                    content += '作者:%s\n' % author
                    print('作者:', author)
                if i == 1:
                    title_l = info.text[2:]
                    content += '標題:%s\n' % title_l
                    print('標題:', title_l)
                if i == 2:
                    datetime = info.text[2:]
                    content += '時間:%s\n' % datetime
                    print('時間:', datetime)

        print('======================================')

        with open('./pttgo/%s.txt' %(title_list.replace('"','-').replace('/','-').replace(':','-').replace('?','')), 'w', encoding='utf-8') as f:
            f.write(content)
    except AttributeError as p:
        print(p)
    except FileNotFoundError as s:
        print(s)
