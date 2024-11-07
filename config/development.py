# -*- coding: utf-8 -*-

DEBUG = False

ENV = 'dev'

LOG_FILE_PATH = '/tmp/flask_demo.log'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rootroot@127.0.0.1:3306/beego_demo?charset=utf8mb4'
SQLALCHEMY_BINDS = {
    'master': 'mysql+pymysql://root:rootroot@127.0.0.1:3306/beego_demo?charset=utf8mb4',
    'slave': 'mysql+pymysql://root:rootroot@127.0.0.1:3306/beego_demo?charset=utf8mb4',
}

DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 100
SQLALCHEMY_POOL_TIMEOUT = 1
SQLALCHEMY_MAX_OVERFLOW = 0
REDIS_URL = 'redis://127.0.0.1:6379/0'


UPLOADS_DEFAULT_DEST = '/static/uploads'
UPLOADS_DEFAULT_URL = 'http://localhost:7070/static/uploads/'
UPLOADED_FILES_ALLOW = 'jpg, png, gif, bmp'
UPLOADED_FILES_DENY = ''
