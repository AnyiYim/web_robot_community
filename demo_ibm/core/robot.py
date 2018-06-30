import datetime

from sqlalchemy import Column, BigInteger, DateTime, String, Integer

from core._mysql import base
import random


class Robot(base):
    __tablename__ = 'robot'
    id = Column(BigInteger, primary_key=True)
    createtime = Column(DateTime, default=datetime.datetime.now())
    model = Column(String(25))
    localX = Column(Integer, default=0)
    localY = Column(Integer, default=0)
    status = Column(Integer, default=0)
    place = Column(String(5))

class RobotMsg(base):
    __tablename__ = 'robot_message'
    id = Column(BigInteger, primary_key=True)
    createtime = Column(DateTime, default=datetime.datetime.now())
    robot_id = Column(BigInteger)
    user_id = Column(BigInteger)
    # localY = Column(Integer, default=0)
    status = Column(Integer, default=1)
