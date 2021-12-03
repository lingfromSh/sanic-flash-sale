from operator import attrgetter

from pydantic import BaseModel
from tortoise.models import Model


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


class ModelSerializer(BaseModel):
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

    def __init_subclass__(cls) -> None:
        metacls = getattr(cls, 'Meta', None)
        assert metacls is not None, 'Missing Meta class.'
        cls.__init_subclass_with_meta_class__(metacls)

    @classmethod
    def __init_subclass_with_meta_class__(cls, metacls) -> None:
        model_cls = getattr(metacls, 'model', None)
        if not issubclass(model_cls, Model):
            raise TypeError("Must be type of tortoise-orm Model.")

        # Set required fields
        for field in REQUIRED_PYDANTIC_CONFIG_FIELDS:
            if not hasattr(metacls, field):
                raise ValueError(f"Missing field: {field}")

            set_config_val(cls.Config, metacls, field)

        # Set optional fields
        for field in OPTIONAL_PYDANTIC_CONFIG_FIELDS:
            if not hasattr(metacls, field):
                continue

            set_config_val(cls.Config, metacls, field)
