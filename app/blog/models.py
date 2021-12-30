import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey

from .database import Base


class BlogModel(Base):
    __tablename__ = "Blogs"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True, name='Id')
    title = sqlalchemy.Column(sqlalchemy.String, name='Title')
    body = sqlalchemy.Column(sqlalchemy.String, name='Body')
    user_id = Column(sqlalchemy.Integer, ForeignKey("Users.UserId"), name='UserId')

    creator = relationship("UserModel", back_populates="blogs", )

class UserModel(Base):
    __tablename__ = 'Users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True, name='UserId')
    name = sqlalchemy.Column(sqlalchemy.String, name='Name')
    email = sqlalchemy.Column(sqlalchemy.String, name='Email')
    password = sqlalchemy.Column(sqlalchemy.String, name='Password')

    blogs = relationship("BlogModel", back_populates="creator")
