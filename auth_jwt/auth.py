import datetime
import jwt

import constants
from itsdangerous import URLSafeTimedSerializer


def create_token(username):
    # Type(Str, Str) -> Str
    headers = {
        'type': 'jwt',
        'alg': 'HS256',
    }
    payload = {
        'username': username,
        'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=1)
    }
    return jwt.encode(payload, key=constants.JWT_SECRET, algorithm='HS256', headers=headers)


def verify_token(token):
    try:
        payload = jwt.decode(token, constants.JWT_SECRET, algorithms=['HS256'])
        print(f'有效的令牌数据：{payload}')
        from flask import g
        g.user = payload
        return True
    except jwt.ExpiredSignatureError:
        print('token 已过期')
        return False
    except jwt.InvalidTokenError:
        print("token 无效")
        return False


def create_web_token(username):
    serializer = __get_jw_serializer()
    return serializer.dumps({
        'username': username,
    })

def verify_web_token(token):
    serializer = __get_jw_serializer()
    serializer.loads(token, max_age=3600)


def __get_jw_serializer():
    return URLSafeTimedSerializer(constants.SERIALIZER_KEY)