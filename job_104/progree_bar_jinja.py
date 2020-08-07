# coding=gbk
from flask import Flask, request, render_template,Response
from ETL.job_104 import progress_bar as p


app = Flask(__name__)

@app.route('/bar', methods=['GET', 'POST'])
def bar():
    request_method = request.method

    bar = dict()
    if request_method == 'GET':

        bar = p.view_bar(1, 20)
        print(bar)
            #view_bar(i, 20)
    return render_template('bar.html', request_method=request_method, bar=bar)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)