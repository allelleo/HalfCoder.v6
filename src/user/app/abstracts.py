"""Файл для хранения абстрактных классов, моделей."""

from tortoise.models import Model

from tortoise.fields import (
    IntField, CharField, DatetimeField
)

class BaseModel(Model):
    """Абстрактный класс для моделей."""

    id = IntField(pk=True)

    class Meta:
        """Класс с метаданными полями."""

        abstract = True


class TimesBaseModel(BaseModel):
    """Абстрактный класс для моделей."""

    time_created = DatetimeField(auto_now_add=True)
    time_updated = DatetimeField(auto_now=True)

    class Meta:
        """Класс с метаданными полями."""

        abstract = True


class RatingBaseModel(TimesBaseModel):
    """Абстрактный класс для моделей."""

    score = IntField(default=0)

    class Meta:
        """Класс с метаданными полями."""

        abstract = True

    async def add_score(self, score):
        """Метод для добавления баллов."""
        pass

    async def update_score(self, score):
        """Метод для обновления баллов."""
        pass

    async def remove_score(self, score):
        """Метод для удаления баллов."""
        pass


class TypeBaseModel(TimesBaseModel):
    """Абстрактный класс для моделей."""

    title = CharField(max_length=40)

    class Meta:
        """Класс с метаданными полями."""

        abstract = True
