from sanic import Request
from common.http.response import JSONResponse


async def health_check(request: Request) -> JSONResponse:
    return JSONResponse(data={
        'db_check': 'ok',
        'redis_check': 'ok'
    })


async def version(request: Request) -> JSONResponse:
    from utils.app import app
    return JSONResponse(data={
        'version': app.config.VERSION
    })