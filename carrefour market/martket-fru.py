from selenium.webdriver import Chrome
import requests
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = Chrome('./chromedriver', chrome_options=chrome_options)
pp=1
total_item_list=[]
for page in range(1,10):

    url = 'https://online.carrefour.com.tw/tw/%E5%AD%A3%E7%AF%80%E6%B0%B4%E6%9E%9C#pageIndex=' + str(pp)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    item_name_list = soup.select('div.commodity-desc')

    item_list = []
    for name in item_name_list:
        item = name.select('a')[0]['title']
        item_re = re.sub(r'\(.*\)|履歷|家樂福|嚴選|進口|台灣|\d.*$|-.*$|#', '', item)
        item_list.append(item_re)

    if item_list==[]:
        print('第%d頁 try again:' %pp)
    else:
        #print(item_list)
        #print(len(item_list))
        total_item_list += item_list
        pp+=1

    # # 判斷若無下一頁則停止
    # page_name_list = soup.select('ul#pagination')
    # page_list = []
    # for page in page_name_list:
    #     s = page.select('li[jp-role="next"]')[0]['class'][0]
    #     try:
    #         if s =='disabled':
    #             print('no next page')
    #
    #
    #     except KeyError as k:
    #         print('check next page')

columns=['種類']
print(total_item_list)
print(len(total_item_list))
df = pd.DataFrame(total_item_list, columns = columns)
df.to_csv('market-fru.csv', index=False, encoding='utf-8-sig')
driver.close()