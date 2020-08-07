# coding=gbk
import requests
from bs4 import BeautifulSoup
import json
import jsonpath
import os

#建立存放資料夾
if not os.path.exists('findjob'):
    os.mkdir('findjob')

def job_list(k,pages):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    # 遍歷所有職缺標題
    bb = []
    for page in range(1, int(pages) + 1):
        url = 'https://www.104.com.tw/area/cj/job/software?area=&jobcategory=&keyword=' + k + '&page=' + str(page)
        #print(url)
        res = requests.get(url, headers=headers)
        res.encoding = 'utf8'
        soup = BeautifulSoup(res.text, 'html.parser')

        url_104 = 'https://www.104.com.tw'
        title_list = soup.select('div.joblist_cont')


        for title in title_list:
            date = title.select_one('div.date').text.replace(' ', '').replace('\n', '')
            com_name = title.select_one('div.compname').text.replace(' ', '').replace('\n', '')
            com_url = url_104 + title.select_one('div.compname').a['href']
            job_name = title.select_one('div.jobname').text.replace(' ', '').replace('\n', '')
            job_url = url_104 + title.select_one('div.jobname').a['href']

            # print('日期:   ', date)
            #print('公司名稱:', com_name)
            # print('公司網址:', com_url)
            #print('職稱名稱:', job_name)
            # print('職稱網址:', job_url)

            # 進入個別職缺的內頁
            job_url_out = job_url.split('/')[-1].split('?')[0]
            job_url_content = 'https://www.104.com.tw/job/ajax/content/' + job_url_out

            headers1 = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                'Referer': 'https://www.104.com.tw/job/6c9yn?jobsource=cj2008', }

            res_content = requests.get(job_url_content, headers=headers1)
            json_data = json.loads(res_content.text)

            comp_name = jsonpath.jsonpath(json_data, '$..custName')[0]
            job_name = jsonpath.jsonpath(json_data, '$..jobName')[0]
            content = jsonpath.jsonpath(json_data, '$..jobDescription')[0]
            money = jsonpath.jsonpath(json_data, '$..salary')[0]
            address = jsonpath.jsonpath(json_data, '$..addressRegion')[0] + jsonpath.jsonpath(json_data, '$..addressDetail')[0]
            exp = jsonpath.jsonpath(json_data, '$..workExp')[0]
            major = jsonpath.jsonpath(json_data, '$..major')[0]
            language = jsonpath.jsonpath(json_data, '$..language[*].language')
            if language==False:
                language=0
            specialty = jsonpath.jsonpath(json_data, '$..specialty[*].description')
            if specialty==False:
                specialty=[]
            #print(specialty)

            ss=[]
            ss.append(comp_name)
            ss.append(job_name)
            ss.append(money)
            ss.append(address)
            ss.append(exp)
            ss.append(major)
            ss.append(language)
            ss.append(specialty)
            #print(ss)
            bb.append(ss)


            content_all = ''
            content_all += '公司名稱:%s\n' % comp_name
            content_all += '職位名稱:%s\n' % job_name
            content_all += '===========================================\n'
            content_all += '工作內容:%s\n' % content
            content_all += '===========================================\n'
            content_all += '公司名稱:%s\n' % comp_name
            content_all += '職位名稱:%s\n' % job_name
            content_all += '工作待遇:%s\n' % money
            content_all += '工作地點:%s\n' % address
            content_all += '工作經歷:%s\n' % exp
            content_all += '科系要求:%s\n' % major
            content_all += '語言條件:%s\n' % language
            #content_all += '擅長工具:%s\n' % specialty

            linux = 0
            MySQL = 0
            Java = 0
            Python = 0
            AWS = 0
            LAN = 0
            MS_SQL=0
            C_sharp=0
            PHP=0
            Github=0
            JavaScript=0

            if specialty==False:
                continue
            else:
                if 'linux' in specialty:
                    linux += 1
                if 'MySQL' in specialty:
                    MySQL += 1
                if 'Java' in specialty:
                    Java += 1
                if 'Python' in specialty:
                    Python += 1
                if 'AWS' in specialty:
                    AWS += 1
                if 'LAN' in specialty:
                    LAN += 1
                if 'MS SQL' in specialty:
                    MS_SQL += 1
                if 'C#' in specialty:
                    C_sharp+= 1
                if 'PHP' in specialty:
                    PHP += 1
                if 'Github' in specialty:
                    Github += 1
                if 'JavaScript' in specialty:
                    JavaScript += 1

                content_all += 'linux:%s\n' % linux
                content_all += 'MySQL:%s\n' % MySQL
                content_all += 'Java:%s\n' % Java
                content_all += 'Python:%s\n' % Python
                content_all += 'AWS:%s\n' % AWS
                content_all += 'LAN:%s\n' % LAN
                content_all += 'MS SQL:%s\n' % MS_SQL
                content_all += 'C#:%s\n' % C_sharp
                content_all += 'PHP:%s\n' % PHP
                content_all += 'Github:%s\n' % Github
                content_all += 'JavaScript:%s\n' % JavaScript

            with open('./findjob/%s.txt' % (comp_name + '_' + job_name).replace(' ', '').replace('/', '').replace(':', '').replace('*', '').replace('|', ''), 'w',encoding='utf-8') as f:
                f.write(content_all)

            # print('工作內容')
            # print(content)
            # print('-------')
            # print('工作待遇:', money)
            # print('工作地點:', address)
            # print('工作經歷:', exp)
            # print('科系要求:', major)
            # print('語言條件:', language)
            # print('擅長工具:', specialty)

            #print('===================================================')
        print('100%')
    return bb


if __name__ == '__main__':
    k = input('請輸入職稱關鍵字:')
    # pages=input('請輸入爬取頁數:')
    pages=2
    job_list(k,pages)


