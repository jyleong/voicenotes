# models.py
# created by James L 07/07/2017

# file for all our database related python objects, used for ORM

import os

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine(os.environ['development_db'])

class User(Base):
    """The test case table in mera_db"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    socketInstanceId = Column(String(60)) # to store the uuid that maps to a websocket instance


    def __init__(self, name):
        self.name = name

    def getSocketInstanceId(self):
        return self.socketInstanceId

    def setSocketInstanceId(self, socketInstanceId):
        self.socketInstanceId = socketInstanceId
