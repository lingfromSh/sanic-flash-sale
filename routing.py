from importlib import import_module
from sanic.blueprints import Blueprint
from common.http.routing import include

routings = [
    'apps.consumer.routing',
    'apps.server.routing',
]

bp = Blueprint.group(list(map(include, routings)), url_prefix='api', version=1)
