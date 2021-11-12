"""
Basic project configuration
"""

import os


# Project conf
PROJECT = 'sanic-flash-sale'
MODE = NotImplemented
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# App registry
INSTALLED_APPS = [
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
        appname: {
            'models': ['models'],
        } for appname in INSTALLED_APPS
    },
    'use_tz': False,
    'timezone': 'UTC'
}