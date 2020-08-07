import requests,os
from bs4 import BeautifulSoup
import json
import jsonpath
import os
from urllib import request

if not os.path.exists('findjob'):
    os.mkdir('findjob')

o_url='https://www.104.com.tw/company/5sq191k?jobsource=cj2008'

url='https://www.104.com.tw/job/ajax/content/6olvl'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
         'Referer':'https://www.104.com.tw/job/6yfdf',}

res = requests.get(url, headers=headers)
json_data=json.loads(res.text)
#print(json_data)

comp_name = jsonpath.jsonpath(json_data, '$..custName')[0]
content = jsonpath.jsonpath(json_data, '$..jobDescription')[0]
money=jsonpath.jsonpath(json_data, '$..salary')[0]
address=jsonpath.jsonpath(json_data, '$..addressRegion')[0]
exp=jsonpath.jsonpath(json_data, '$..workExp')[0]
major=jsonpath.jsonpath(json_data, '$..major')[0]
language=jsonpath.jsonpath(json_data, '$...language')[0]
specialty=jsonpath.jsonpath(json_data, '$..specialty[*].description')

content_all=''
content_all+='公司名稱:%s\n' %comp_name
content_all+='===========================================\n'
content_all+='工作內容:%s\n' %content
content_all+='===========================================\n'
content_all+='工作待遇:%s\n' %money
content_all+='工作地點:%s\n' %address
content_all+='工作經歷:%s\n' %exp
content_all+='科系要求:%s\n' %major
content_all+='語言條件:%s\n' %language
content_all+='擅長工具:%s\n' %specialty

with open('./findjob/%s.txt' % (comp_name), 'w', encoding='utf-8') as f:
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
