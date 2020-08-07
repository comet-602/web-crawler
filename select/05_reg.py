from bs4 import BeautifulSoup
import re
a = '''
<div>
    <p>段落1</p>
    <p>段落2</p>
    <h>
       <a href='xxx.biaoti.com'>Re:標题1</a>
       <a href='www.biaoti.com'>Re:標题2</a>
    </h>
    <h>
       <a href='www.biaogame.com'>Re:標题_a</a>
       <a href='www.biaogame.com'>Re:標题_b</a>
    </h>
    <a href='www.biaogame333.pnp'>Re:標题3</a>
    <a href='www.biaogame444.jpg'>Re:標题4</a>

</body>
'''
soup = BeautifulSoup(a, 'html.parser')
#直接將指定的標籤(該標籤需要有多個)作為串列，並利用串列選擇需要的位置
print('1==================================')
print(soup.select('a[href^=xxx]')) # 多层嵌套也可以直接返回
print(soup.find_all('a',{"href":re.compile("^x")})) # 多层嵌套也可以直接返回
print('2=================================')
print(soup.select_one('a')['href']) # 多层嵌套也可以直接返回
print(soup.find('a')['href'])
print('3=================================')
xt=soup.select('a[href^=xxx]')
for i in xt:
    print(i['href'])
print('------------------------')
xt=soup.find_all('a',{"href":re.compile("jpg$")})
for i in xt:
    print(i['href'])
print('------------------------')
xt=soup.select('a[href]')
for i in xt:
    if re.match(r'^w',i['href']):
        print(i['href'])