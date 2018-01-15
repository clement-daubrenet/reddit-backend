from flask import Blueprint
from flask_io import fields
from sqlalchemy_utils.functions import sort_query
from uuid import uuid4
from .models import Topic
from .schemas import TopicSchema
from .. import db, io

app = Blueprint('topics', __name__, url_prefix='/topics')
  

@app.route('/', methods=['POST'])
@io.from_body('topic', TopicSchema)
@io.marshal_with(TopicSchema)
def add_topic(topic):
    topic.id = str(uuid4())
    db.session.add(topic)
    db.session.commit()
    return topic


@app.route('/', methods=['GET'])
@io.from_query('author', fields.String())
@io.from_query('order_by', fields.String(missing='name'))
@io.from_query('offset', fields.Integer(missing=0))
@io.from_query('limit', fields.Integer(missing=10))
@io.marshal_with(TopicSchema, envelope=True)
def get_topics(author, order_by, offset, limit):
    query = Topic.query
    if author:
        query = query.filter(Topic.author == author)

    if order_by:
        query = sort_query(query, order_by)

    if offset:
        query = query.offset(offset)

    if limit:
        query = query.limit(limit)
    return query.all()
