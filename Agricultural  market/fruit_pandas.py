# coding=gbk
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import sys
from tqdm import tqdm


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
         'Referer':'https://amis.afa.gov.tw/fruit/FruitProdDayTransInfo.aspx'}
url='https://amis.afa.gov.tw/fruit/FruitProdDayTransInfo.aspx'
cookies={'ASP.NET_SessionId':'tutwky4mwc4pj0mywhqzybvg'}

res=requests.get(url,headers=headers,cookies=cookies)
soup = BeautifulSoup(res.text, 'html.parser')
#��ȡ���[�ؙ�λ
view_state=soup.select('input#__VIEWSTATE')[0]['value']
event_validation=soup.select('input#__EVENTVALIDATION')[0]['value']

Product="ȫ���aƷ"
ProductNo="ALL"

data={"ctl00$ScriptManager_Master":"ctl00$ScriptManager_Master|ctl00$contentPlaceHolder$btnQuery",
    "__EVENTTARGET":	"",
    "__EVENTARGUMENT":	"",
    "__VIEWSTATE":	view_state,
    "__VIEWSTATEGENERATOR":	"A4896558",
    "__EVENTVALIDATION":	event_validation,
    "ctl00$contentPlaceHolder$ucDateScope$rblDateScope":	"P",
    "ctl00$contentPlaceHolder$ucSolarLunar$radlSolarLunar":	"S",
    "ctl00$contentPlaceHolder$txtSTransDate":	"109/06/10",
    "ctl00$contentPlaceHolder$txtETransDate":	"109/06/11",
    "ctl00$contentPlaceHolder$txtMarket":	"ȫ���Ј�",
    "ctl00$contentPlaceHolder$hfldMarketNo":	"ALL",
    "ctl00$contentPlaceHolder$txtProduct":	Product,
    "ctl00$contentPlaceHolder$hfldProductNo":	ProductNo,
    "ctl00$contentPlaceHolder$hfldProductType":	"A",
    "__ASYNCPOST":	"true",
    "ctl00$contentPlaceHolder$btnQuery":	"��ԃ"}

#time.sleep(0.2)
res_post=requests.post(url,headers=headers,cookies=cookies,data=data)

soup = BeautifulSoup(res_post.text, 'html.parser')

first_time=time.time()
if soup.select('div#ctl00_contentPlaceHolder_panel') == []:
    print('�o�Y��')
else:
    TransDate = soup.select('span#ctl00_contentPlaceHolder_lblTransDate')[0].text
    Markets = soup.select('span#ctl00_contentPlaceHolder_lblMarkets')[0].text
    Products = soup.select('span#ctl00_contentPlaceHolder_lblProducts')[0].text

    detail_item = soup.select('table[style="border-color: Gray;"]')[0].select('tr')[2:]
    info_list=[TransDate,Markets,]


    columns=['��ԃ��������', '��ԃ�Ј�', '����', '�Ј�', '�aƷ', '�σr', '�Ѓr', '�r', 'ƽ���r(Ԫ/����)', '��ǰһ�����ձ��^%', '������(����)',
                 '��ǰһ�����ձ��^%']
    total_list=[]
    for i in detail_item:
        #time.sleep(0.1)

        item_list=info_list+[j.text for j in i.select('td')]
        total_list.append(item_list)
        df = pd.DataFrame(total_list, columns = columns)

        #print('===================')

    df.to_csv('fruit_pandas1.csv', index=False, encoding='utf-8-sig')  # Ҫ��utf-8-sig�D�����Ų������_CSV�n�y�a
    pbar = tqdm(total_list)
    for c in pbar:
        time.sleep(0.1)
        pbar.set_description("Processing")

    #print(total_list)
    last_time = time.time()
    print(last_time-first_time)




