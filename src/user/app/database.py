"""Файл с настройками для базы данных."""

from tortoise.contrib.fastapi import register_tortoise
from tortoise.models import Model
from fastapi import FastAPI


def init(app: FastAPI):
    """Функция для инициализации базы данных."""
    register_tortoise(
        app,
        db_url='sqlite://database.db',
        modules={'models': ['app.api.v1.models']},
        generate_schemas=True,
        add_exception_handlers=True,
    )
