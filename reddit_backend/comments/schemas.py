from flask_io import fields, Schema, post_load
from .models import Comment


class CommentSchema(Schema):

    id = fields.UUID(dump_only=True)
    author = fields.String(30)
    message = fields.String(required=True)
    post_id = fields.UUID(required=True, as_text=True)

    @post_load
    def _post_load(self, data):
        return Comment(**data)
