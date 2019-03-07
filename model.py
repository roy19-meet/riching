from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  full_name = Column(String)
  email = Column(String)       
  age = Column(Integer)
  gender = Column(String)
  is_working = Column(Boolean)
  is_full_student = Column(Boolean)

class income(Base):
  __tablename__="incomes"
  id = Column(Integer,primary_key=True)
  amount = Column(Integer)


class outcome(Base):
  __tablename__="outcomes"
  id = Column(Integer,primary_key=True)
  amount = Column(Integer)

	
		


