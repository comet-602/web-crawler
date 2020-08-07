import requests,os
from bs4 import BeautifulSoup



url='https://news.google.com/topstories?hl=zh-TW&tab=wn&gl=TW&ceid=TW:zh-Hant'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

htmls=soup.select('div[jsname="V2bVMb"]')[0]
for html in htmls:
    if 'aria-label' in html.attrs:
        title=html.attrs['aria-label']
        url_re='https://news.google.com/'+html.select("a")[0]["href"][2:]
        print(title)
        print(url)
        re=requests.get(url_re)
        soup_re=BeautifulSoup(re.text,'html.parser')

        content=soup_re.select('h3')
        for cont in content:
            print(cont.text)

        print('===================================')

