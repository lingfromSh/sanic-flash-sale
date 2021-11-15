from tortoise import fields
from common.database.models import BaseModel


class Category(BaseModel):

    class Meta:
        table_name = 'categories'

    name = fields.CharField(max_length=255)
    desc = fields.TextField()
    parent = fields.ForeignKeyField('product.Category', on_delete=fields.CASCADE)
    sort_order = fields.IntField()

class Attribute(BaseModel):

    class Meta:
        table_name = 'attributes'
    
    name = fields.CharField(max_length=255)
    simple_desc = fields.CharField(max_length=128)
    full_desc = fields.TextField()


class Spu(BaseModel):

    class Meta:
        table_name = 'spus'

    category = fields.ForeignKeyField('product.Category', on_delete=fields.RESTRICT)
    attributes = fields.ManyToManyField('product.Attribute', through='spu_sku_attributes')
    main_image = fields.CharField(max_length=255)
    code = fields.CharField(max_length=255)
    name = fields.CharField(max_length=255)
    desc = fields.CharField(max_length=255)
    is_on_sale = fields.BooleanField(default=False)


class Sku(BaseModel):

    class Meta:
        table_name = 'products'

    spu = fields.ForeignKeyField('product.Sku', on_delete=fields.CASCADE)
    code = fields.CharField(max_length=255)
    main_image = fields.CharField(max_length=255)
    thumbnail_image = fields.CharField(max_length=255)
    price = fields.DecimalField(max_digits=19, decimal_places=2)
    inventory = fields.BigIntField(default=0)
    desc = fields.CharField(max_length=255)
    is_on_sale = fields.BooleanField(default=False)


class SpuSkuAttribute(BaseModel):

    class Meta:
        table_name = 'spu_sku_attributes'

    spu = fields.ForeignKeyField('product.Spu', on_delete=fields.CASCADE)
    attribute = fields.ForeignKeyField('product.Attribute', on_delete=fields.CASCADE)
    sku = fields.ForeignKeyField('product.Sku', on_delete=fields.CASCADE, related_name='attributes')
    value = fields.CharField(max_length=255)