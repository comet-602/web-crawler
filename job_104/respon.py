import flask
import time

from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
import sys

app = flask.Flask(__name__)

@app.route('/yield')
def index():
    def inner():
        for x in range(10):
            time.sleep(0.5)
            t = sys.stdout.write(str(x))
            t = sys.stdout.flush()
        yield t

    env = Environment(loader=FileSystemLoader('templates'))
    tmpl = env.get_template('result.html')
    return flask.Response(tmpl.generate(result=inner()))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
