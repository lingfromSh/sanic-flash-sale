from typing import AnyStr, Dict, List, Union

import orjson
import status as http_status
from sanic.response import HTTPResponse


class JSONResponse(HTTPResponse):

    status = http_status.HTTP_200_OK

    def __init__(self, data: Union[Dict, List, AnyStr], msg="ok") -> None:
        super().__init__(
            body=orjson.dumps({
                'data':data,
                'message': msg
            }), 
            status=self.status,
            content_type='application/json'
        )


class CreatedJSONResponse(JSONResponse):

    status = http_status.HTTP_201_CREATED


class AcceptedJSONResponse(JSONResponse):

    status = http_status.HTTP_202_ACCEPTED


class NoContentJSONResponse(JSONResponse):

    status = http_status.HTTP_204_NO_CONTENT


class UnAcceptableJSONResponse(JSONResponse):

    status = http_status.HTTP_206_PARTIAL_CONTENT


class MovedPermanentlyJSONResponse(JSONResponse):

    status = http_status.HTTP_301_MOVED_PERMANENTLY


class BadRequestJSONResponse(JSONResponse):

    status = http_status.HTTP_400_BAD_REQUEST


class UnAuthorizedJSONResponse(JSONResponse):

    status = http_status.HTTP_401_UNAUTHORIZED


class ForbiddenJSONResponse(JSONResponse):

    status = http_status.HTTP_403_FORBIDDEN


class NotFoundJSONResponse(JSONResponse):

    status = http_status.HTTP_404_NOT_FOUND


class ServerErrorJSONResponse(JSONResponse):

    status = http_status.HTTP_500_INTERNAL_SERVER_ERROR
