from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.sql import func
start = datetime.utcnow()


class Blog(Base):
    __tablename__ = "Blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(16), index=True)
    body = Column(String(16), index=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    creator = relationship("User", back_populates="Blogs")


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), index=True)
    email = Column(String(64), index=True)
    password = Column(String(64), index=True)

    Blogs = relationship("Blog", back_populates="creator")


class Timekeeping(Base):
    __tablename__ = 'timekeeping'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), index=True)
    timekeeping = Column(DateTime(timezone=True), server_default=func.utcnow())

    # time_timekeeping = Column(datetime)

