from tortoise import fields
from common.database.models import BaseModel
from apps.permission.choices import ActionTypeEnum, DataTypeTypeEnum


class Role(BaseModel):

    class Meta:
        table_name = 'roles'

    name = fields.CharField(max_length=255)
    code = fields.CharField(max_length=255, unique=True)
    desc = fields.TextField()
    allowed_actions = fields.ManyToManyField('permission.Action', through='role_actions')


class Group(BaseModel):

    class Meta:
        table_name = 'groups'

    name = fields.CharField(max_length=255)
    code = fields.CharField(max_length=255, unique=True)
    desc = fields.TextField()
    allowed_actions = fields.ManyToManyField('permission.Action', through='group_actions')


class Action(BaseModel):

    class Meta:
        table_name = 'actions'

    type = fields.IntEnumField(ActionTypeEnum)
    name = fields.CharField(max_length=255)
    code = fields.CharField(max_length=255)
    desc = fields.TextField()


class DataType(BaseModel):

    class Meta:
        table_name = 'data_types'

    type = fields.IntEnumField(DataTypeTypeEnum)


class ActionParam(BaseModel):

    class Meta:
        table_name = 'action_params'
    
    action = fields.ForeignKeyField('permission.Action', on_delete=fields.CASCADE)
    type = fields.ForeignKeyField('permission.DataType', on_delete=fields.RESTRICT)
    code = fields.CharField(max_length=255)
    constraints = fields.ManyToManyField('permission.PermissionConstraint', through='action_param_constraints', on_delete=fields.CASCADE)
    desc = fields.TextField()


class PermissionConstraint(BaseModel):

    class Meta:
        table_name = 'permission_constraints'

    type = fields.ForeignKeyField('permission.DataType', on_delete=fields.CASCADE)
    code = fields.CharField(max_length=255, unique=True)
    func = fields.TextField()
    func_params = fields.JSONField()
    desc = fields.TextField()


class ActionParamConstraint(BaseModel):

    class Meta:
        table_name = 'action_param_constraints'

    action_param = fields.ForeignKeyField('permission.ActionParam', on_delete=fields.RESTRICT)
    constraint = fields.ForeignKeyField('permission.PermissionConstraint', on_delete=fields.RESTRICT)
    constraint_settings = fields.JSONField()


class RoleAction(BaseModel):

    class Meta:
        table_name = 'role_actions'

    role = fields.ForeignKeyField('permission.Role', on_delete=fields.CASCADE)
    action = fields.ForeignKeyField('permission.Action', on_delete=fields.RESTRICT)
    # Allowed value for this (role, action)
    value = fields.JSONField()


class GroupAction(BaseModel):

    class Meta:
        table_name = 'group_actions'
    
    group = fields.ForeignKeyField('permission.Group', on_delete=fields.CASCADE)
    action = fields.ForeignKeyField('permission.Action', on_delete=fields.RESTRICT)
    # Allowed value for this (role, action)
    value = fields.JSONField()
