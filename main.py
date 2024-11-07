import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'], endpoint='index')
def index():
    return render_template('index.html', id=random.randint(1, 1000))

@app.route("/info/<id>", endpoint='detail', methods=['GET'])
def get_info(id):
    data = {
        'id': id,
        'title': '详情页面',
    }
    return render_template('info.html', **data)


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)