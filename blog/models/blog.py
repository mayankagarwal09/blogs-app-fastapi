from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from ..database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key= True, index= True)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean, default= False)

    username = Column(String, ForeignKey('users.username'))

    creator = relationship('User', back_populates="blogs")