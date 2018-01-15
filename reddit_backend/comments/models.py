from .. import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, ForeignKey, String, text
from datetime import datetime


class Comment(db.Model):
    __tablename__ = 'post_comments'

    id = Column(UUID, primary_key=True)
    author = Column(String(30), nullable=False)
    message = Column(String(), nullable=False)
    post_id = Column(ForeignKey('posts.id', ondelete='CASCADE'), nullable=False)
    created = Column(DateTime(True), nullable=False, default=datetime.now, server_default=text("now()"))

    post = relationship('Post', lazy='noload')
