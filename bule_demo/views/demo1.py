import random

from flask import Blueprint, render_template

from models.model import Book

bp = Blueprint('view_demo1', __name__,  url_prefix='/demo1/view')

@bp.route('/list')
def list_demo():
    books = Book.query.order_by(Book.id.desc()).all()

    data = []
    for book in books:
        data.append({
            'id': book.id,
            'title': book.title,
            'content': book.content,
        })
    return render_template('list.html', books=data)