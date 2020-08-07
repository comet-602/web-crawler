import requests,os
from bs4 import BeautifulSoup



url='https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiUENCSVNOam9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q3hJSkwyMHZNREl6TW1ob2Vnc0tDUzl0THpBeU16Sm9hQ2dBKjEIACotCAoiJ0NCSVNGem9JYkc5allXeGZkako2Q3dvSkwyMHZNREl6TW1ob0tBQVABUAE?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
cookies={'over18':'1'}
res = requests.get(url, headers=headers,cookies=cookies)
soup = BeautifulSoup(res.text, 'html.parser')


print(soup.text)