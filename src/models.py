# models.py
# created by James L 07/07/2017

# file for all our database related python objects, used for ORM

import os

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine(os.environ['development_db'])

class Message(Base):
    """The message table in mera_db"""
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    messageContent = Column(String(255))


    def __init__(self, text):
        self.messageContent = text

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)



