from tortoise import fields
from tortoise.models import Model
from utils.snowflake import generate_unique_id


class BaseModel(Model):

    id = fields.BigIntField(default=generate_unique_id)
    
    created = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)