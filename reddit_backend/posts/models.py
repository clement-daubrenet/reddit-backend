from .. import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text
from datetime import datetime


class Post(db.Model):
    __tablename__ = 'posts'

    id = Column(UUID, primary_key=True, autoincrement=True)
    title = Column(String(64))
    author = Column(String(30))
    message = Column(String())
    up_vote = Column(Integer(), default=0, nullable=False)
    down_vote = Column(Integer(), default=0, nullable=False)
    topic_id = Column(ForeignKey('topics.id', ondelete='CASCADE'), nullable=False)
    created = Column(DateTime(True), nullable=False, default=datetime.now, server_default=text("now()"))

    topic = relationship('Topic', lazy='noload')
