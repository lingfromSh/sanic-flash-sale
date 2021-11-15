from tortoise import fields
from apps.form.choices import BasicTypeEnum
from common.database.models import BaseModel


class Form(BaseModel):

    class Meta:
        table_name = 'forms'

    name = fields.CharField(max_length=255)
    code = fields.CharField(max_length=255, unique=True)
    desc = fields.TextField()

    is_enabled = fields.BooleanField(default=True)


class Field(BaseModel):

    class Meta:
        table_name = 'fields'

    name = fields.CharField(max_length=255)
    code = fields.CharField(max_length=255, unique=True)
    desc = fields.TextField()
    type = fields.ForeignKeyField('form.FieldType', on_delete=fields.RESTRICT)
    constraints = fields.ManyToManyField('form.FormConstraint', through='field_constraints')


class FieldType(BaseModel):

    class Meta:
        table_name = 'field_types'

    name = fields.CharField(max_length=255)
    code = fields.CharField(max_length=255, unique=True)
    desc = fields.TextField()
    constraints = fields.ManyToManyField('form.FormConstraint', through='field_type_constraints')


class BasicType(BaseModel):

    class Meta:
        table_name = 'basic_types'

    name = fields.CharField(max_length=255)
    type = fields.IntEnumField(BasicTypeEnum)
    constraints = fields.ManyToManyField('form.FormConstraint', through='basic_type_constraints')


class FormConstraint(BaseModel):

    class Meta:
        table_name = 'form_constraints'

    name = fields.CharField(max_length=255)
    func = fields.TextField()
    func_params = fields.JSONField()
    desc = fields.TextField()


class FieldConstraint(BaseModel):

    class Meta:
        table_name = 'field_constraints'

    field = fields.ForeignKeyField('form.Field', on_delete=fields.CASCADE)
    constraint = fields.ForeignKeyField('form.FormConstraint', on_delete=fields.RESTRICT)
    settings = fields.JSONField()


class FieldTypeConstraint(BaseModel):

    class Meta:
        table_name = 'field_type_constraints'

    field_type = fields.ForeignKeyField('form.FieldType', on_delete=fields.CASCADE)
    constraint = fields.ForeignKeyField('form.FormConstraint', on_delete=fields.RESTRICT)
    default_settings = fields.JSONField()
    
    is_required = fields.BooleanField(default=False)
    is_setting_overriable = fields.BooleanField(default=True)


class BasicTypeConstraint(BaseModel):

    class Meta:
        table_name = 'basic_type_constraints'

    basic_type = fields.ForeignKeyField('form.BasicType', on_delete=fields.CASCADE)
    constraint = fields.ForeignKeyField('form.FormConstraint', on_delete=fields.RESTRICT)
    default_settings = fields.JSONField()
    
    is_required = fields.BooleanField(default=False)
    is_setting_overriable = fields.BooleanField(default=True)

