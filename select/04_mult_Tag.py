from bs4 import BeautifulSoup
import re
a = '''
<div>
    <p>段落1</p>
    <p>段落2</p>
    <h>
       <a href='www.biaoti.com'>Re:標题1</a>
    </h>
    <h>
       <a href='www.biaogame.com'>Re:標题2</a>
    </h>
    <a href='www.biaogame333.pnp'>Re:標题3</a>
    <a href='www.biaogame444.jpg'>Re:標题4</a>

</body>
'''
soup = BeautifulSoup(a, 'html.parser')
#直接將指定的標籤(該標籤需要有多個)作為串列，並利用串列選擇需要的位置
print(soup.select('div p')[1].text)
print('0==================================')
# 提取内容
#print(soup.p.text)
for p in soup.select('p'):
    print(p.text)
print('1==================================')
print(soup.select('h')) # 多层嵌套也可以直接返回
print(soup.find_all('h')) # 多层嵌套也可以直接返回
print('11=================================')
print(soup.select('h')[0]) # 多层嵌套也可以直接返回
print(soup.find_all('h')[0]) # 多层嵌套也可以直接返回
print(soup.select('h')[1]) # 多层嵌套也可以直接返回
print(soup.find_all('h')[1]) # 多层嵌套也可以直接返回
print('2==================================')
print(soup.select('h')[0].a) # 也可以这样
print(soup.find_all('h')[0].a) # 也可以这样
print(soup.select('h')[1].a) # 也可以这样
print(soup.find_all('h')[1].a) # 也可以这样
print('3==================================')
print(soup.select('h')[0].a.text) # 里面有多个内容时 '\n标题\n段落1\n段落2\n'
print(soup.select('h')[1].a.text)
print(soup.find_all('h')[0].a.text)
print(soup.find_all('h')[1].a.text)
print('4==================================')
for i in soup.select('h'):
    print(i)
for i in soup.find_all('h'):
    print(i)
print('a------------------------------------')
for i in soup.select('h'):
    print(i.select('a')) #各子標籤各轉為串列
for i in soup.find_all('h'):
    print(i.find_all('a')) #各子標籤各轉為串列
print('b------------------------------------')
for i in soup.select('h'):
    print(i.select('a')[0])
    print(i.a)  #兩種寫法
for i in soup.find_all('h'):
    print(i.find_all('a')[0])
    print(i.a)  #兩種寫法
print('c------------------------------------')
for i in soup.select('h'):
    print(i.select('a')[0].text)
    print(i.a.text) #兩種寫法
for i in soup.find_all('h'):
    print(i.find_all('a')[0].text)
    print(i.a.text)
print('d------------------------------------')
for i in soup.select('h'):
    print(i.select('a')[0]['href'])
    print(i.a['href']) #兩種寫法
for i in soup.find_all('h'):
    print(i.find_all('a')[0]['href'])
    print(i.a['href']) #兩種寫法
print('4==================================')
# 提取属性值，像字典一样提取，以下两种方法等价
print(soup.select('h')[0].a['href'])
print(soup.select('h')[1].a['href'])
print(soup.find_all('h')[0].a['href'])
print(soup.find_all('h')[1].a['href'])
print(soup.h.a.get('href'))
print('5==================================')
for i in soup.select('a'):
    print(i['href'])
