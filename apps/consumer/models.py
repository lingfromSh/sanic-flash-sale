from tortoise import fields
from common.database.models import BaseModel


class Consumer(BaseModel):

    class Meta:
        table_name = 'consumers'
    
    mobile = fields.CharField(max_length=11, unique=True)
    hashed_password = fields.CharField(max_length=255)
    roles = fields.ManyToManyField('permission.Role', through='consumer_roles')
    is_soft_delete = fields.DatetimeField(null=True)


class ConsumerAddress(BaseModel):

    class Meta:
        table_name = 'consumer_addresses'

    province = fields.ForeignKeyField('common.Province', on_delete=fields.RESTRICT)
    city = fields.ForeignKeyField('common.City', on_delete=fields.RESTRICT)
    district = fields.ForeignKeyField('common.District', on_delete=fields.RESTRICT)
    street = fields.ForeignKeyField('common.Street', on_delete=fields.RESTRICT)
    detail = fields.TextField()

    name = fields.CharField(max_length=255)
    mobile = fields.CharField(max_length=11)

    tags = fields.JSONField()
    is_default = fields.BooleanField(default=True)
    sort_order = fields.SmallIntField()


class ConsumerRole(BaseModel):

    class Meta:
        table_name = 'consumer_roles'

    consumer = fields.ForeignKeyField('consumer.Consumer')
    role = fields.ForeignKeyField('permission.Role')
    validity = fields.DatetimeField(auto_now_add=True)
    expiration = fields.DatetimeField()
