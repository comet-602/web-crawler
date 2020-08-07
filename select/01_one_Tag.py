from bs4 import BeautifulSoup
a = '''
<h1>標題1</h1>
<h2>標題2</h2>
<h2>標題3</h2>
'''

soup = BeautifulSoup(a, "html.parser")

# 提取唯一標籤
print(soup.h1)
print(soup.find('h1'))
print(soup.find_all('h1'))
print(soup.find_all('h1')[0])
print('========================')
print(soup.select('h1'))
print(soup.select('h1')[0])
print('========================')
print(soup.find_all('h2'))
print(soup.find_all(['h1','h2']))