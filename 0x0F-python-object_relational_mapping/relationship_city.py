#!/usr/bin/python3
"""  Improved the file model_city.py with relationship class attribute """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """ class State that inherits from Base (from model_state) """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
