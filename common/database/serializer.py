from operator import attrgetter
from typing import no_type_check, Optional

from pydantic import BaseModel
from pydantic.main import ModelMetaclass
from tortoise.models import Model

from .field_annotation_converter import field_annotation

REQUIRED_PYDANTIC_CONFIG_FIELDS = [
    'title',
]

OPTIONAL_PYDANTIC_CONFIG_FIELDS = [
    'anystr_strip_whitespace',
    'anystr_lower',
    'min_anystr_length',
    'max_anystr_length',
    'validate_all',
    'extra',
    'allow_mutation',
    'use_enum_values',
    'fields',
    'validate_assignment',
    'allow_population_by_field_name',
    'getter_dict',
    'alias_generator',
    'keep_untouched',
    'schema_extra',
    'error_msg_templates',
    'arbitrary_types_allowed',
    'json_loads',
    'json_dumps',
    'json_encoders'
]


def set_config_val(config_cls, metacls, field):
    getter = attrgetter(field)
    setattr(config_cls, field, getter(metacls))


def is_required(field):
    return field.pk or getattr(field, "null", None) is not None


class ModelSerializerMetaclass(ModelMetaclass):
    @no_type_check  # noqa C901
    def __new__(mcs, name, bases, namespace, **kwargs):
        mcs.__init_subclass_fields_with_meta_cls__(name, bases, namespace, **kwargs)
        new_cls = super().__new__(mcs, name, bases, namespace, **kwargs)
        return new_cls

    @classmethod
    def __init_subclass_fields_with_meta_cls__(mcs, name, bases, namespace, **kwargs):
        metacls = namespace.get("Meta", None)
        if not metacls:
            return
        
        model_cls = getattr(metacls, 'model', None)
        if not issubclass(model_cls, Model):
            raise TypeError("Must be type of tortoise-orm Model.")

        annotations = {}
        for name, field in model_cls.get_fields_map().items():
            ann = field_annotation(field)
            annotations.update({
                name: ann if is_required(field) else Optional[ann]
            })

        namespace.update(__annotations__=annotations)


class ModelSerializer(BaseModel, metaclass=ModelSerializerMetaclass):
    """
    Examples:
    >>> class ConsumerModelSerializer(ModelSerializer):
    >>>     '''
    >>>     A model serializer for consumer tortoise-orm model
    >>>     '''
    >>>
    >>>     class Meta:
    >>>         model = Consumer
    >>>         fields = Optional[List]
    >>>         excludes = Optional[List]
    >>>         extra_fields = Optional[List]
    >>>     
    """

    class Config:
        orm_mode = True
