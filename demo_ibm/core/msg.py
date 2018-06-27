import datetime

from sqlalchemy import Column, BigInteger, DateTime, String, Boolean

from core._mysql import base


class Msg(base):
    __tablename__ = 'message'
    id = Column(BigInteger, primary_key=True)
    createtime = Column(DateTime, default=datetime.datetime.now())
    message = Column(String(255))
    user_id = Column(BigInteger)
    call = Column(String(255))
    flag = Column(Boolean, default=True)

