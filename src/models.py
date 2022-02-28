import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(255))
    author_id = Column(Integer, ForeignKey('User.id'))
    post_id = Column(Integer, ForeignKey('Post.id'))
    user = relationship('User')
    post = relationship('Post')

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    # comment_text = Column(String(255))
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship('User')

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    media_type = Column(Integer)
    url = Column(String(255))
    post_id = Column(Integer, ForeignKey('Post.id'))
    post_id_rel = relationship('Post')

class Follower(Base):
    __tablename__ = 'Follower'
    id = Column(Integer, primary_key=True)
    # comment_text = Column(String(255))
    person_id = Column(Integer, ForeignKey('User.id'))
    user = relationship('User')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e