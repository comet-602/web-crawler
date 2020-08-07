# coding=gbk
from flask import Flask, request, render_template
from ETL.job_104 import j4_combine as c

app = Flask(__name__)

@app.route('/content', methods=['GET', 'POST'])
def pokers():
    request_method = request.method

    jobs = dict()
    if request_method == 'POST':
        k = request.form.get('k')
        pages = request.form.get('pages')
        jobs = c.job_list(k,pages)
    return render_template('content.html', request_method=request_method, jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)