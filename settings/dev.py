"""
Dev project configuration
"""

from settings.base import *

# Project conf
MODE = 'dev'
WORKER_ID = 0
CENTER_ID = 0

# Databases conf
POSTGRES = {
    'connections': {
        # Dict format for connection
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': 'localhost',
                'port': '5432',
                'user': 'root',
                'password': 'password',
                'database': 'postgres',
            }
        },
    },
    'apps': {
        appname.split('.')[1]: {
            'models': [f'{appname}.models'],
        } for appname in INSTALLED_APPS
    },
    'use_tz': False,
    'timezone': 'UTC'
}


# Redis conf
REDIS = {
    'host': '',
    'port': '',
    'dbindex': '',
    'password': '',
}

# Mongodb conf
MONGODB = {
    'host': '',
    'port': '',
    'password': ''
}

# Security conf
# NOTE: in this project, i choose bearer token as jwt token.
JWT_ENCODE_SECRET = 'N2pZESDCKwF2+YRo82Z/QTcfBm1U/d5SBrCvdjfMXYY='
JWT_ENCODE_ALGORITHM = 'HS512'

# ARGON2
PASSWORD_HASH_ALGORITHM = 'argon2'
PASSWORD_HASH_SALT = 'YJxh8Dmzjpk+tCEf8JNe5LPF/NzFniCQO3R4WvkUvso='

# BAIDU Map
BAIDU_MAP_API_KEY = 'aIGVNVLqcOPmYPTpDEllUSIF12rjBoc4'
BAIDU_MAP_SECRET_KEY = '58Z27PxiY4p0VL8aMCD6HhpvA0mxibLD'