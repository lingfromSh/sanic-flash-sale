from tortoise import fields
from common.database.models import BaseModel
from apps.store.choices import ApprovalStatusEnum


class Store(BaseModel):

    class Meta:
        table_name = 'stores'
    
    name = fields.CharField(max_length=255)


class StoreBusinessInfo(BaseModel):

    class Meta:
        table_name = 'store_business_infos'

    name = fields.CharField(max_length=255)
    business_code = fields.CharField(max_length=255)
    business_license = fields.CharField(max_length=255)
    status = fields.IntEnumField(ApprovalStatusEnum)
