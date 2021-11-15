from tortoise import fields
from apps.admin.choices import AccountStatusEnum
from common.database.models import BaseModel


class StoreAdmin(BaseModel):

    class Meta:
        table_name = 'store_admins'
        unique_together = ('store', 'username')

    store = fields.ForeignKeyField('store.Store', on_delete=fields.CASCADE)
    username = fields.CharField(max_length=255)
    mobile = fields.CharField(max_length=255, unique=True)
    email = fields.CharField(max_length=255, unique=True)
    hashed_password = fields.CharField(max_length=255)
    status = fields.IntEnumField(AccountStatusEnum)
    roles = fields.ManyToManyField('permission.Role', on_delete=fields.CASCADE)
    groups = fields.ManyToManyField('permission.Group', on_delete=fields.CASCADE)


class PlatformAdmin(BaseModel):

    class Meta:
        table_name = 'platform_admins'

    username = fields.CharField(max_length=255, unique=True)
    hashed_password = fields.CharField(max_length=255)
    mobile = fields.CharField(max_length=255, unique=True)
    email = fields.CharField(max_length=255, unique=True)
    status = fields.IntEnumField(AccountStatusEnum)
    roles = fields.ManyToManyField('permission.Role', on_delete=fields.CASCADE)
    groups = fields.ManyToManyField('permission.Group', on_delete=fields.CASCADE)
