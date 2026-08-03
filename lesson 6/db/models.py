from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean, Float, Text

from db.config import Base

class BaseModel(Base):
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
class Admins(BaseModel):
    __tablename__ = 'admins'
    
    name = Column(Text)
    email = Column(Text)

class Lists(BaseModel):
    __tablename__ = 'gh_list'
    
    name = Column(Text)
    
class Online(BaseModel):
    __tablename__ = 'online'
    
    timestamp = Column(DateTime)
    name = Column(Text)
    level = Column(Integer)
    last_login = Column(DateTime)
    is_online = Column(Boolean)
    
