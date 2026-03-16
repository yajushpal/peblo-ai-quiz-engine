from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Question(Base):

    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    type = Column(String)
    options = Column(JSON)
    answer = Column(String)
    difficulty = Column(String)
    source_chunk = Column(String)