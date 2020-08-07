from flask import Flask,request
import requests
from bs4 import BeautifulSoup

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_post():
    request_method = request.method   #偵測用甚麼進行訪問
    outStr = ''
    if request_method == 'GET':
        outStr="""
        <body>
            <form action="hello_post" method="POST">
                <label>What Job do you want to find?</label>
                <br></br>
                <input type="textbox" name="name">
                <button type="submit">SUBMIT</button>
            </form>
        </body>
        """
        return outStr
    elif request_method=='POST':
        outStr="""
        <body>
            <form action="hello_post" method="POST">
                <label>What is your name?</label>
                <br></br>        
                <input type="textbox" name="name">
                <button type="submit">SUBMIT</button>
            </form>
        """
        name=request.form.get('name')  #帶的資料取出字串，放入底下Hello後

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        url = 'https://www.104.com.tw/area/cj/job/software?keyword=' + name + '&jobcategory=&area='

        res = requests.get(url, headers=headers)
        res.encoding = 'utf8'
        soup = BeautifulSoup(res.text, 'html.parser')

        url_104 = 'https://www.104.com.tw'
        title_list = soup.select('div.joblist_cont')

        for title in title_list:
            job_name=title.select_one('div.jobname').text.replace(' ', '').replace('\n', '')
            outStr+=job_name
        return outStr

#加上'debug=True' 不須重新啟動即可更新資料
if __name__=='__main__':
    app.run(debug=True,host='localhost',port=5000)