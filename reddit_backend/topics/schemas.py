from flask_io import fields, Schema, post_load

from .models import Topic


class TopicSchema(Schema):
    id = fields.UUID(dump_only=True)
    title = fields.String(64)

    @post_load
    def _post_load(self, data):
        return Topic(**data)
