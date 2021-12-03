from sanic import Request
from sanic.views import HTTPMethodView

from apps.consumer.models import Consumer
from apps.consumer.serializers import ConsumerModelSerializer
from common.http.response import JSONResponse


class ConsumerView(HTTPMethodView):
    """
    Works for consumer's everything.
    """

    async def get(self, request: Request, id: int, *args, **kwargs) -> JSONResponse:
        consumer = await Consumer.get_or_none(id=id)
        serializer= ConsumerModelSerializer.from_orm(consumer)
        return JSONResponse(data=serializer.json())


async def login(request: Request) -> JSONResponse:
    """
    For consumers' log in.
    """
    print(request)
    serializer = None
    return JSONResponse(data=serializer)


async def register(request: Request) -> JSONResponse:
    """
    For consumers' registering in.
    """
    print(request)
    serializer = None
    return JSONResponse(data=serializer)
