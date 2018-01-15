from flask import Blueprint
from uuid import uuid4
from flask_io import fields
from .schemas import PostSchema
from .models import Post
from .. import db, io

app = Blueprint('posts', __name__, url_prefix='/posts')


@app.route('/', methods=['POST'])
@io.from_body('post', PostSchema)
@io.marshal_with(PostSchema)
def add_post(post):
    post.id = str(uuid4())
    # Store the new post in the database
    db.session.add(post)
    db.session.commit()
    return post


@app.route('/', methods=['GET'])
@io.from_query('topic_id', fields.UUID(as_text=True))
@io.from_query('offset', fields.Integer(missing=0))
@io.marshal_with(PostSchema, envelope=True)
def get_posts(topic_id, offset):
    query = Post.query
    if topic_id:
        query = query.filter(Post.topic_id == topic_id)

    if offset:
        query = query.offset(offset)

    return query.all()


@app.route('/<uuid:post_id>', methods=['GET'])
@io.marshal_with(PostSchema)
def get_post(post_id):
    query = Post.query
    if post_id:
        query = query.filter(Post.id == str(post_id))
    return query.first()


@app.route('/upvote/<uuid:post_id>', methods=['POST'])
@io.marshal_with(PostSchema)
def upvote_post(post_id):
    post = Post.query.filter(Post.id == str(post_id)).first()
    post.up_vote += 1
    db.session.add(post)
    db.session.commit()
    return post


@app.route('/downvote/<uuid:post_id>', methods=['POST'])
@io.marshal_with(PostSchema)
def downvote_post(post_id):
    post = Post.query.filter(Post.id == str(post_id)).first()
    post.down_vote += 1
    db.session.add(post)
    db.session.commit()
    return post
