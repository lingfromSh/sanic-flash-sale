import os
from sanic import Sanic
from sanic.response import HTTPResponse
from common.settings import YamlConfig

config = YamlConfig(os.environ.get("SANIC_CONFIGURATION_PATH"))
application = Sanic(config.PROJECT.NAME, config=config)


@application.get("/health-check/", strict_slashes=True)
async def health_check(request):
    return HTTPResponse("ok", content_type="application/json")