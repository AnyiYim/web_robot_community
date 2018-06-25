import datetime

from sqlalchemy import Column, BigInteger, DateTime, String,Boolean

from core._mysql import base


class Resident(base):
    __tablename__ = 'resident'
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger)
    true_name = Column(String(25))
    telephone = Column(String(32))
    address = Column(String(255))
    building = Column(String(25))
    sex = Column(Boolean, default=True)
