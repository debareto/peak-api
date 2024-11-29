from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Peak(Base):

    __tablename__ = 'peaks'

    id= Column(Integer, primary_key = True, index = True) 
    name = Column(String)
    latitude = Column(Float, nullable  = False)
    longitude = Column(Float,  nullable  = False)
    elevation = Column(Float,  nullable  = False)