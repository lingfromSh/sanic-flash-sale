from tortoise import fields
from common.database.models import BaseModel


class Consumer(BaseModel):

    class Meta:
        table_name = "consumers"
    
    mobile = fields.CharField(max_length=11, unique=True)
    hashed_password = fields.CharField(max_length=255)


class ConsumerAddress(BaseModel):

    class Meta:
        table_name = "consumer_addresses"

    city = fields.IntEnumField()
    region = fields.IntEnumField()
    detail = fields.TextField()

    name = fields.CharField(max_length=255)
    mobile = fields.CharField(max_length=11)

    tags = fields.CharField(max_length=255)
    is_default = fields.BooleanField(default=True)
    sort_order = fields.SmallIntField()
