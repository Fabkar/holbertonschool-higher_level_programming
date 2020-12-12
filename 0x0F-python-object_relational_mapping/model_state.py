#!/usr/bin/python3
"""Define a State model.
    Inherits from SQLAlchemy Base and links to the MySQL table states."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Respresent a state for MySQL database.
    __tablename__ (str): The name of the MySQL table to store States.
    id (integer): The State's id.
    name (str): The state's name.
    """
    __tablename__ = "states"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement="auto")
    name = Column(String(128), nullable=False)
