"""Модель данных для запроса сущности должность."""
from pydantic import BaseModel


class PositionModelResp(BaseModel):
    """Модель данных для запроса сущности должность."""
    id: int
    title: str