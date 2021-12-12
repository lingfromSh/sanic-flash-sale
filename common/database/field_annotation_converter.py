import decimal
from functools import singledispatch
from tortoise import fields


@singledispatch
def field_annotation(field):
    pass


@field_annotation.register(fields.SmallIntField) 
@field_annotation.register(fields.IntField)
@field_annotation.register(fields.BigIntField)
def convert_to_int(field):
    return int


@field_annotation.register(fields.CharField)
def convert_to_str(field):
    return str


@field_annotation.register(fields.BooleanField)
def convert_to_bool(field):
    return bool


@field_annotation.register(fields.FloatField)
def convert_to_float(field):
    return float


@field_annotation.register(fields.DecimalField)
def convert_to_decimal(field):
    return decimal

