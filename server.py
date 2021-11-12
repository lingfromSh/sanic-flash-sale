import argparse

from sanic import Sanic
from sanic.config import Config
from sanic.response import HTTPResponse
from tortoise.contrib.sanic import register_tortoise

# Collect command line args
parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mode', default='dev', help='Which mode to start with?')
args = parser.parse_args()

# Collect config
config = Config()
config.update_config(f"settings/{args.mode}.py")

# Init sanic app
application = Sanic('sanic-flash-sale', config=config, strict_slashes=True)

# Register tortoise for sanic.
register_tortoise(application, config=application.config.POSTGRES, generate_schemas=True)


# Register health check url
@application.get("/health-check/")
async def health_check(request):
    return HTTPResponse("ok", content_type="application/json")


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8000, access_log=True)
