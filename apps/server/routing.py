from apps.server.blueprint import bp
from apps.server.handlers import health_check, version


bp.add_route(health_check, 'health-check/', name='health-check')
bp.add_route(version, 'version/', name='version')