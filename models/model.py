from sqlalchemy import Integer, Column, String

from common.routing import RouteSQLAlchemy

db = RouteSQLAlchemy()


class Book(db.Model):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
