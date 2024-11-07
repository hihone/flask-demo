from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify

import auth_jwt.auth
from decoration import require_user_login

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('')
def login():
    return render_template('login.html')

@bp.route('/sign/in', methods=['POST'], endpoint='sign_in')
def sign_in():
    if request.method != 'POST':
        return redirect(url_for('login'))
    username = request.form.get('username', '')
    if not username:
        return {'code': 400, 'message': '用户名不能为空'}
    password = request.form.get('password', '')
    if not password:
        return {'code': 400, 'message': '密码不能为空'}

    if username != 'hihone' or password != '123456':
        return {'code': 400, 'message': '用户名或密码错误'}

    token = auth_jwt.auth.create_token(username)
    session['token'] = token

    return {'code': 0, 'message': '登录成功', 'token': token}

@bp.route('/show/token')
@require_user_login
def show_token():
    token = session.get('token')
    return jsonify(code=0, token=token)