from .. import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, SmallInteger


class Topic(db.Model):
    __tablename__ = 'topics'

    id = Column(UUID, primary_key=True)
    title = Column(String(64))
