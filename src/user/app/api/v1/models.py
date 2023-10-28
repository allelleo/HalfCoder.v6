"""Файл с моделями для базы данных."""

from tortoise.fields import (
    IntField, CharField, ForeignKeyField,
    ManyToManyField, OneToOneField, BinaryField, BooleanField, UUIDField
)
import bcrypt
from app.abstracts import TimesBaseModel, RatingBaseModel, TypeBaseModel
from app.sugar import override
import uuid

class Profile(TimesBaseModel):
    """Модель профиля."""

    work = CharField(max_length=100, default='Не указано')
    sex = CharField(max_length=3, default='nil')
    age = IntField(default=-1)
    education = CharField(max_length=100, default='Не указано')
    hobby = CharField(max_length=100, default='Не указано')
    quote = CharField(max_length=180, default='Не указано')
    phone = CharField(max_length=11, default='Не указано')
    country = CharField(max_length=100, default='Не указано')
    website = CharField(max_length=100, default='Не указано')

    class Meta:
        """Класс с метаданными полями."""

        table = 'profile'


class Rating(RatingBaseModel):
    """Модель рейтинга."""

    @override
    async def add_score(self, score):
        """Метод для добавления баллов."""
        pass

    @override
    async def update_score(self, score):
        """Метод для обновления баллов."""
        pass

    @override
    async def remove_score(self, score):
        """Метод для удаления баллов."""
        pass

    class Meta:
        """Класс с метаданными полями."""

        table = 'rating'


class RatingPerWeek(RatingBaseModel):
    """Модель рейтинга по неделям."""

    @override
    async def add_score(self, score):
        """Метод для добавления баллов."""
        pass

    @override
    async def update_score(self, score):
        """Метод для обновления баллов."""
        pass

    @override
    async def remove_score(self, score):
        """Метод для удаления баллов."""
        pass

    class Meta:
        """Класс с метаданными полями."""

        table = 'rating_per_week'


class RatingPerMonth(RatingBaseModel):
    """Модель рейтинга по месяцам."""

    @override
    async def add_score(self, score):
        """Метод для добавления баллов."""
        pass

    @override
    async def update_score(self, score):
        """Метод для обновления баллов."""
        pass

    @override
    async def remove_score(self, score):
        """Метод для удаления баллов."""
        pass

    class Meta:
        """Класс с метаданными полями."""

        table = 'rating_per_month'


class Politic(TimesBaseModel):
    """Модель политики."""

    email = IntField(default=0)
    work = IntField(default=0)
    age = IntField(default=0)
    education = IntField(default=0)
    hobby = IntField(default=0)
    phone = IntField(default=0)
    country = IntField(default=0)
    website = IntField(default=0)

    class Meta:
        """Класс с метаданными полями."""

        table = 'politic'


class BookMarkType(TypeBaseModel):
    """Модель типа закладки."""

    class Meta:
        """Класс с метаданными полями."""

        table = 'bookmark_type'


class BookMark(TimesBaseModel):
    """Модель закладки."""

    to_id = IntField(default=0)
    bookmark_type = ForeignKeyField('models.BookMarkType')

    class Meta:
        """Класс с метаданными полями."""

        table = 'bookmark'


class LikeType(TypeBaseModel):
    """Модель типа лайка."""

    class Meta:
        """Класс с метаданными полями."""

        table = 'like_type'


class Like(TimesBaseModel):
    """Модель лайка."""

    to_id = IntField(default=0)
    like_type = ForeignKeyField('models.LikeType')

    class Meta:
        """Класс с метаданными полями."""

        table = 'like'


class SubscriptionType(TypeBaseModel):
    """Модель типа подписки."""

    class Meta:
        """Класс с метаданными полями."""

        table = 'subscription_type'


class Subscription(TimesBaseModel):
    """Модель подписки."""

    to_id = IntField(default=0)
    subscription_type = ForeignKeyField('models.SubscriptionType')

    class Meta:
        """Класс с метаданными полями."""

        table = 'subscription'


class NotificationType(TypeBaseModel):
    """Модель типа уведомления."""

    class Meta:
        """Класс с метаданными полями."""

        table = 'notification_type'


class Notification(TimesBaseModel):
    """Модель уведомления."""

    title = CharField(max_length=100)
    description = CharField(max_length=100)
    notification_type = ForeignKeyField('models.NotificationType')

    class Meta:
        """Класс с метаданными полями."""

        table = 'notification'

class EmailValidation(TimesBaseModel):
    """Модель валидации почты."""

    code = CharField(max_length=40)
    done = BooleanField(default=False)


class User(TimesBaseModel):
    """Модель пользователя."""

    username = CharField(max_length=30)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    password = BinaryField()
    email = CharField(max_length=30)
    email_validated = BooleanField(default=False)
    uuid = UUIDField(default=uuid.uuid4)

    profile = OneToOneField('models.Profile')
    rating = OneToOneField('models.Rating')
    ratingWeek = OneToOneField('models.RatingPerWeek')
    ratingMonth = OneToOneField('models.RatingPerMonth')
    politic = OneToOneField('models.Politic')

    bookmarks = ManyToManyField('models.BookMark')
    notifications = ManyToManyField('models.Notification')
    likes = ManyToManyField('models.Like')
    subscribes = ManyToManyField('models.Subscription')
    emails = ManyToManyField('models.EmailValidation')

    async def set_password(self, password):
        """Функция для изменения пароля пользователя."""
        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.password = password
        return True

    async def check_password(self, password):
        """Функция для проверки пароля пользователя."""
        result = bcrypt.checkpw(password.encode('utf-8'), self.password)
        if result:
            return True
        return False
