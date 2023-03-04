from sqlalchemy import Column, VARCHAR, INTEGER, DATE, ForeignKey, BigInteger
from .base import BaseModel
import datetime


class Task(BaseModel):
    __tablename__ = 'tasks'

    id = Column(INTEGER(), primary_key=True, autoincrement=True)
    admin_id = Column(BigInteger())
    queue = Column(INTEGER(), default=0)
    posts = Column(INTEGER(), default=0)
    date = Column(DATE, default=datetime.date.today())


class Msg(BaseModel):
    __tablename__ = 'messages'

    id = Column(INTEGER(), primary_key=True, autoincrement=True)
    task = Column(INTEGER(), ForeignKey('tasks.id'))
    msg_id = Column(VARCHAR(30))
    queue = Column(INTEGER())
    date = Column(DATE, default=datetime.date.today())
