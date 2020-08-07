# coding=gbk
import requests
from bs4 import BeautifulSoup
import time
import csv


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
         'Referer':'https://amis.afa.gov.tw/fruit/FruitProdDayTransInfo.aspx'}
url='https://amis.afa.gov.tw/fruit/FruitProdDayTransInfo.aspx'
cookies={'ASP.NET_SessionId':'tutwky4mwc4pj0mywhqzybvg'}

res=requests.get(url,headers=headers,cookies=cookies)
soup = BeautifulSoup(res.text, 'html.parser')
#先取得隱藏欄位
view_state=soup.select('input#__VIEWSTATE')[0]['value']
event_validation=soup.select('input#__EVENTVALIDATION')[0]['value']

Product="全部產品"
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
    "ctl00$contentPlaceHolder$txtMarket":	"全部市場",
    "ctl00$contentPlaceHolder$hfldMarketNo":	"ALL",
    "ctl00$contentPlaceHolder$txtProduct":	Product,
    "ctl00$contentPlaceHolder$hfldProductNo":	ProductNo,
    "ctl00$contentPlaceHolder$hfldProductType":	"A",
    "__ASYNCPOST":	"true",
    "ctl00$contentPlaceHolder$btnQuery":	"查詢"}

#time.sleep(0.2)
res_post=requests.post(url,headers=headers,cookies=cookies,data=data)

soup = BeautifulSoup(res_post.text, 'html.parser')

if soup.select('div#ctl00_contentPlaceHolder_panel') == []:
    print('無資料')
else:
    TransDate = soup.select('span#ctl00_contentPlaceHolder_lblTransDate')[0].text
    Markets = soup.select('span#ctl00_contentPlaceHolder_lblMarkets')[0].text
    Products = soup.select('span#ctl00_contentPlaceHolder_lblProducts')[0].text

    detail_item = soup.select('table[style="border-color: Gray;"]')[0].select('tr')[2:]
    info_list=[TransDate,Markets,]

    with open('output.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('查詢交易日期','查詢市場','日期','市場','產品', '上價', '中價', '下價', '平均價(元/公斤)', '跟前一交易日比較%', '交易量(公斤)', '跟前一交易日比較%'))

        for i in detail_item:
            #time.sleep(0.1)
            item_list=info_list+[j.text for j in i.select('td')]
            print(item_list)
            print('===================')
            writer.writerow(item_list)


    # print('交易日期：', TransDate)
    # print('市　　場：', Markets)
    # print('產　　品：', Products)
    #print(detail_item[23:31])






