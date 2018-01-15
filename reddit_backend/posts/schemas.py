from flask_io import fields, Schema, post_load
from .models import Post


class PostSchema(Schema):

    id = fields.UUID(dump_only=True)
    author = fields.String(30, required=True)
    title = fields.String(64, required=True)
    message = fields.String(required=True)
    topic_id = fields.UUID(required=True, as_text=True)
    up_vote = fields.Integer(dump_only=True)
    down_vote = fields.Integer(dump_only=True)
    created = fields.DateTime(dump_only=True)

    @post_load
    def _post_load(self, data):
        return Post(**data)
