from .. import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String


class Topic(db.Model):
    __tablename__ = 'topics'

    id = Column(UUID, primary_key=True)
    title = Column(String(64))
