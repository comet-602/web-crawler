import requests,os
from bs4 import BeautifulSoup
import json
import jsonpath
import os
from urllib import request

if not os.path.exists('findjob'):
    os.mkdir('findjob')

#https://www.104.com.tw/job/6y4xr?jobsource=cj2008
url='https://www.104.com.tw/job/ajax/content/6y4xr'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
         'Referer':'https://www.104.com.tw/job/6c9yn?jobsource=cj2008',}

res = requests.get(url, headers=headers)
json_data=json.loads(res.text)
#print(json_data)

comp_name = jsonpath.jsonpath(json_data, '$..custName')[0]
job_name = jsonpath.jsonpath(json_data, '$..jobName')[0]
content = jsonpath.jsonpath(json_data, '$..jobDescription')[0]
money = jsonpath.jsonpath(json_data, '$..salary')[0]
address = jsonpath.jsonpath(json_data, '$..addressRegion')[0] + jsonpath.jsonpath(json_data, '$..addressDetail')[0]
exp = jsonpath.jsonpath(json_data, '$..workExp')[0]
major = jsonpath.jsonpath(json_data, '$..major')[0]
language = jsonpath.jsonpath(json_data, '$..language[*].language')
specialty = jsonpath.jsonpath(json_data, '$..specialty[*].description')


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
content_all += '擅長工具:%s\n' % specialty

linux = 0
MySQL = 0
Java = 0
Python = 0
AWS = 0
LAN = 0
MS_SQL = 0
C_sharp = 0
PHP = 0
Github = 0
JavaScript = 0

if specialty!=False:

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
        C_sharp += 1
    if 'PHP' in specialty:
        PHP += 1
    if 'Github' in specialty:
        Github += 1
    if 'JavaScript' in specialty:
        JavaScript += 1






with open('./findjob/%s.txt' % (comp_name + '_' + job_name).replace(' ', '').replace('/', '').replace(':', ''), 'w',
          encoding='utf-8') as f:
    f.write(content_all)


print('工作內容')
print(content)
print('=======================================')
print('工作待遇:',money)
print('工作地點:',address)
print('工作經歷:',exp)
print('科系要求:',major)
print('語言條件:',language)
print('擅長工具:',specialty)
# print('Linux:%d' %Linux)
# print('MySQL:%d' %MySQL)