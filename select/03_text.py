from bs4 import BeautifulSoup
a = '''
<p id='p1'>段落1</p>
<p class='p3'>段落2</p>
<p class='p3'>文章</p>
<p></p>
'''

soup = BeautifulSoup(a, "html.parser")

print(soup.find_all('p', text='文章'))
print(soup.find_all('p', text=['段落1','段落2']))