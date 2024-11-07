# -*- coding: utf-8 -*-
import sqlalchemy.orm as orm
from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy, BaseQuery
from sqlalchemy import engine

MASTER_DB = 'master'
SLAVE_DB = 'slave'
FIXED_SLAVE_BINDS = 'fixed_slave'

class TipsOrmQuery(orm.query.Query):
    #  这个只是提示  真实返回值为  orm.query.Query 的方法

    def filter(self, *criterion) -> TipsOrmQuery: ...

    def join(self, *props, **kwargs) -> TipsOrmQuery: ...

    def order_by(self, *criterion) -> TipsOrmQuery: ...

    def label(self, name) -> TipsOrmQuery: ...

    def limit(self, limit) -> TipsOrmQuery: ...

    def offset(self, offset) -> TipsOrmQuery: ...


class TipsOrmBaseQuery(BaseQuery):
    #  这个只是提示  真实返回值为  BaseQuery 的方法

    def filter(self, *criterion) -> TipsOrmBaseQuery: ...

    def join(self, *props, **kwargs) -> TipsOrmBaseQuery: ...

    def order_by(self, *criterion) -> TipsOrmBaseQuery: ...

    def label(self, name) -> TipsOrmBaseQuery: ...

    def limit(self, limit) -> TipsOrmBaseQuery: ...

    def offset(self, offset) -> TipsOrmBaseQuery: ...


class TipsOrmModel(object):
    # 这个只是提示  真实返回为  flask_sqlalchemy/__init__.py:800
    query: TipsOrmBaseQuery


class TipsOrmSession(orm.session.Session):
    def query(self, *entities, **kwargs) -> TipsOrmQuery: ...


class TipsOrmEngine(engine.Engine):
    # 这个只是提示  真实返回为 sqlalchemy.engine.base.Engine 的方法

    def execute(self, statement, *multiparams, **params) -> engine.ResultProxy: ...


class SQLAlchemy(_BaseSQLAlchemy):
    # 这个只是提示  真实返回为  flask_sqlalchemy/__init__.py:715
    session: TipsOrmSession
    # 这个只是提示  真实返回为  flask_sqlalchemy/__init__.py:716
    Model: TipsOrmModel


class RouteSQLAlchemy(SQLAlchemy):

    # 这个只是提示  真实返回为  common.routing.RouteSQLAlchemy.engine
    @property
    def engine(self) -> TipsOrmEngine: ...
