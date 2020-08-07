import requests,os
from bs4 import BeautifulSoup

if not os.path.exists('news'):
    os.mkdir('news')

url='https://tw.appledaily.com/hot/daily/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

top_url='https://tw.appledaily.com'
top_list=soup.select('div[class="aht_menu"]')[0]

for i in range(0,7):
    top_name=top_list.select('a')[i].text
    y = top_list.select('a')[i]['href']
    top_list_url=top_url+y
    print(top_name)
    res = requests.get(top_list_url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    for i in soup.select('div[class="aht_board"] li'):
        index = i.select('div', class_=["aht_title_num atopred", "aht_title_num"])[0].text
        title = i.select('div[class="aht_title"]')[0].text
        url = i.select('div[class="aht_title"]')[0].a['href']
        print(index, title)
        print(url)
        print('============================================')

        if not os.path.exists('./news/%s'%top_name):
            os.mkdir('./news/%s'%top_name)

        with open('./news/%s/%s.txt' % (top_name,title.replace('/', '').replace('?', '')), 'w', encoding='utf-8') as f:
            f.write('Hello world')
