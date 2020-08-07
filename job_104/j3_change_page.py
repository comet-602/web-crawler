import requests
from bs4 import BeautifulSoup
import json
import os
from urllib import request
k=input('請輸入職稱關鍵字:')
pages=input('請輸入爬取頁數:')

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

for page in range(1,int(pages)+1):
    url = 'https://www.104.com.tw/area/cj/job/software?area=&jobcategory=&keyword=' + k + '&page=' + str(page)
    print(url)
    res = requests.get(url, headers=headers)
    res.encoding = 'utf8'
    soup = BeautifulSoup(res.text, 'html.parser')

    url_104 = 'https://www.104.com.tw'
    title_list = soup.select('div.joblist_cont')

    for title in title_list:
        print('日期:   ', title.select_one('div.date').text.replace(' ', '').replace('\n', ''))
        print('公司名稱:', title.select_one('div.compname').text.replace(' ', '').replace('\n', ''))
        print('公司網址:', url_104 + title.select_one('div.compname').a['href'])
        print('職稱名稱:', title.select_one('div.jobname').text.replace(' ', '').replace('\n', ''))
        print('職稱網址:', url_104 + title.select_one('div.jobname').a['href'])
        print('===================================================')
    print('換頁')


