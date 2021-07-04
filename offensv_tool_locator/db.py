from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class CVElist(Base):
    __tablename__ = "cve"
    id = Column(Integer, primary_key=True)
    repo = Column(String(50))
    about = Column(Text)
    created_date = Column(DateTime)
    gh_stars = Column(Integer)


class Rat(Base):
    __tablename__ = "rat"
    id = Column(Integer, primary_key=True)
    repo = Column(String(50))
    about = Column(Text)
    created_date = Column(DateTime)
    gh_stars = Column(Integer)



db = create_engine('sqlite:///db.sqlite3', echo=True)
Base.metadata.create_all(bind=db)
Session = sessionmaker(bind=db)
session = Session()
