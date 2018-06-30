import datetime

from sqlalchemy import Column, Integer, DateTime, String, BigInteger
from sqlalchemy.orm import relationship

from core._mysql import base


class car(base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    createtime = Column(DateTime, default=datetime.datetime.now())
    licenseplace = Column(String(10))
    brand = Column(String(25))
    user_id = Column(BigInteger)

    user = relationship('User', foreign_keys=[user_id],
                        primaryjoin='User.id==car.user_id',
                        lazy='joined')
