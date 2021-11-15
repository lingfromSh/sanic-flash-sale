from enum import IntEnum


class ActionTypeEnum(IntEnum):

    URL = 0
    DATABASE = 1


class DataTypeTypeEnum(IntEnum):

    STRING = 0
    INT = 1
    FLOAT = 2
    DICT = 3
    LIST = 4
    BOOL = 5
