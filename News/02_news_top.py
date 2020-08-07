import requests
from bs4 import BeautifulSoup


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
    print(top_list_url)
