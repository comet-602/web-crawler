import requests
from bs4 import BeautifulSoup
import json
import os
from urllib import request
k=''
def title(k):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    url = 'https://www.104.com.tw/area/cj/job/software?keyword=' + k + '&jobcategory=&area='

    res = requests.get(url, headers=headers)
    res.encoding = 'utf8'
    soup = BeautifulSoup(res.text, 'html.parser')

    url_104 = 'https://www.104.com.tw'
    title_list = soup.select('div.joblist_cont')
    ss = []
    for title in title_list:

        date=title.select_one('div.date').text.replace(' ', '').replace('\n', '')
        com_name=title.select_one('div.compname').text.replace(' ', '').replace('\n', '')
        com_url=url_104 + title.select_one('div.compname').a['href']
        job_name=title.select_one('div.jobname').text.replace(' ', '').replace('\n', '')
        job_url=url_104 + title.select_one('div.jobname').a['href']

        ss.append(job_name)

        print('日期:   ',date)
        print('公司名稱:', com_name)
        print('公司網址:', com_url)
        print('職稱名稱:', job_name)
        print('職稱網址:', job_url)
        print('===================================================')

    return ss

if __name__ == '__main__':
    title(k)



