import requests
from bs4 import BeautifulSoup

url='https://m.thsrc.com.tw/tw/TimeTable/SearchResult'

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}

data={"startStation":"977abb69-413a-4ccf-a109-0272c24fd490",
       "endStation":"2f940836-cedc-41ef-8e28-c2336ac8fe68",
       "theDay":"2020/05/25",
       "timeSelect":"19:00",
       "waySelect":"DepartureInMandarin"}
res_post=requests.post(url,data=data,headers=headers)

soup=BeautifulSoup(res_post.text,'html.parser')

print(soup)