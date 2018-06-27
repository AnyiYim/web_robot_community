import datetime

from sqlalchemy import Column, BigInteger, DateTime, String

from core._mysql import base


class Role(base):
    __tablename__ = 'role'
    id = Column(BigInteger, primary_key=True)
    role = Column(String(255))

