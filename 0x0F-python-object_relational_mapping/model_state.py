#!/usr/bin/python3
"""
this module for hbtn_0e_6_usa
"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    this class for table states
    """
    __tablename__ = "states"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128))
