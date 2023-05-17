from .log import LoggingMiddleware
from .request_id import RequestIdMiddleware

middlewares = [
    {"middleware": RequestIdMiddleware, "args": {}},
    {"middleware": LoggingMiddleware, "args": {}},
]
