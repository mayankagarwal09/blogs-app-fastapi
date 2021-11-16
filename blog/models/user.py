from sqlalchemy.orm import relationship
from ..database import Base
from sqlalchemy import Column, String

class User(Base):
    __tablename__ = 'users'
    
    username = Column(String, primary_key= True, index=True)
    name = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates="creator")