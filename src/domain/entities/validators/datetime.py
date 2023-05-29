from datetime import datetime, timezone

from pydantic.datetime_parse import parse_datetime


class CustomDatetime:
    @classmethod
    def __get_validators__(cls):
        yield parse_datetime
        yield cls.ensure_tzinfo

    @classmethod
    def ensure_tzinfo(cls, value):
        # TODO: Validar timezone das configurações
        if value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)
        return value.astimezone(timezone.utc)

    @staticmethod
    def to_str(dt: datetime) -> str:
        return dt.isoformat()
