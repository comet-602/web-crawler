from flask import Flask, request, render_template

from ETL.job_104 import j1_title as p

app = Flask(__name__)

@app.route('/title', methods=['GET', 'POST'])
def pokers():
    request_method = request.method

    cards = dict()
    if request_method == 'POST':
        k = request.form.get('k')
        cards = p.title(k)
        print(cards)
    return render_template('title.html', request_method=request_method,cards=cards)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)