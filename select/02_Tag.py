from bs4 import BeautifulSoup
a = '''
<p id='p1'>段落1</p>
<p id='p2'>段落2</p>
<p class='p3'>段落3</p>
<p class='p3' id='pp'>段落4</p>
'''
soup = BeautifulSoup(a, "html.parser")

# 第一種，直接將属性名作為參數名，但是有些属性不行，比如像a-b這樣的属性
print(soup.find_all('p', id = 'p1')) # 一般情况
print(soup.find_all('p', class_='p3')) # class是保留字比较特殊，需要后面加一個_
print('====================================')
# 最通用的方法，attrs可加可不加
#                   標籤      屬性
print(soup.find_all('p', {'class':'p3'}))
print(soup.find_all('p', attrs={'class':'p3'})) # 包含这个属性就算，而不是只有这个属性
print(soup.find_all('p', attrs={'class':'p3','id':'pp'})) # 使用多个属性匹配
print(soup.find_all('p', attrs={'class':'p3','id':False})) # 指定不能有某个属性
print(soup.find_all('p', attrs={'id':['p1','p2']})) # 属性值是p1或p2
print(soup.find_all('p', {'id':['p1','p2']}))       # 属性值是p1或p2
print(soup.find_all('p', id=['p1','p2']))           # 属性值是p1或p2