from functools import wraps

from flask import session, jsonify

from auth_jwt import auth


def require_user_login(f):
    @wraps(f)
    def decorator_function(*args, **kwargs):
        token = session.get('token')
        if not token or token == '':
            return jsonify(code=401, messages='请先登录')
        if not auth.verify_token(token):
            return jsonify(code=401, messages='token 已失效')
        return f(*args, **kwargs)

    return decorator_function
