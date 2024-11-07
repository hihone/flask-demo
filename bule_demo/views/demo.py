import random

from flask import Blueprint, render_template

bp = Blueprint('view_demo', __name__,  url_prefix='/demo/view')

@bp.route('', endpoint='index')
def index():
    return render_template("index.html", id=random.randint(1, 100))

@bp.route('/info/<id>', endpoint='detail', methods=['GET'])
def info(id):
    data = {
        'id': id,
        'title': '详情',
    }
    return render_template('info.html', **data)