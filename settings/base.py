"""
Basic project configuration
"""

import os


# Project conf
PROJECT = 'sanic-flash-sale'
MODE = NotImplemented
VERSION = '0.0.1'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(BASE_DIR, 'resources')

# App registry
INSTALLED_APPS = [
    'apps.admin',
    'apps.common',
    'apps.consumer',
    'apps.form',
    'apps.permission',
    'apps.product',
    'apps.store',
]

# Database conf
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