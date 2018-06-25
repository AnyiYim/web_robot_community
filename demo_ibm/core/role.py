import datetime

from sqlalchemy import Column, BigInteger, DateTime, String

from core._mysql import base


class Role(base):
    __tablename__ = 'role'
    id = Column(BigInteger, primary_key=True)
    # createtime = Column(DateTime, default=datetime.datetime.now())
    role = Column(String(255))
    # day = Column(String(25))
    # true_name = Column(String(25))
    # telephone = Column(String(32))
    # address = Column(String(255))
    # password_md = Column(String(255))
