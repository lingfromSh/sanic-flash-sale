from tortoise import fields
from common.database.models import BaseModel


class Province(BaseModel):

    class Meta:
        table_name = 'provinces'

    name = fields.CharField(max_length=255, unique=True)
    code = fields.IntField(unique=True)

class City(BaseModel):

    class Meta:
        table_name = 'cities'

    city = fields.ForeignKeyField('common.Province', on_delete=fields.CASCADE)
    name = fields.CharField(max_length=255, unique=True)
    code = fields.IntField(unique=True)


class District(BaseModel):

    class Meta:
        table_name = 'districts'

    city = fields.ForeignKeyField('common.City', on_delete=fields.CASCADE)
    name = fields.CharField(max_length=255, unique=True)
    code = fields.IntField(unique=True)


class Street(BaseModel):

    class Meta:
        table_name = 'streets' 

    district = fields.ForeignKeyField('common.District', on_delete=fields.CASCADE)
    name = fields.CharField(max_length=255, unique=True)
    code = fields.IntField(unique=True)
