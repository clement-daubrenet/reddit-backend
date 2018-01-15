from flask import Blueprint
from flask_io import fields
from uuid import uuid4
from .models import Comment
from .schemas import CommentSchema
from .. import db, io

app = Blueprint('comments', __name__, url_prefix='/comments')


@app.route('/', methods=['GET'])
@io.from_query('post_id', fields.UUID(as_text=True))
@io.marshal_with(CommentSchema, envelope=True)
def get_comments(post_id):
    query = Comment.query
    if post_id:
        query = query.filter(Comment.post_id == str(post_id))
    return query.all()


@app.route('/', methods=['POST'])
@io.from_body('comment', CommentSchema)
@io.marshal_with(CommentSchema)
def add_commnents(comment):
    comment.id = str(uuid4())
    db.session.add(comment)
    db.session.commit()
    return comment
