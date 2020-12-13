#!/usr/bin/python3
"""Define a City model.
    Inherits from SQLAlchemy Base and links to the MySQL table states."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ Respresent a city for MySQL database.

    Attributes:
    id (str): The city's id.
    name: The city's name.
    state_id : the city's state id.
    """
    __tablename__ = "cities"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement="auto")
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
