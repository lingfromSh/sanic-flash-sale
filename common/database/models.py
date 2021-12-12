from tortoise import fields
from tortoise.models import Model, ModelMeta
from utils.snowflake import generate_unique_id


class BaseModel(Model, metaclass=ModelMeta):

    id = fields.BigIntField(pk=True, default=generate_unique_id)
    
    created = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)

    @classmethod
    def get_fields_map(cls):
        return cls._meta.fields_map