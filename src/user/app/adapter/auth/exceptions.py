"""Файл ошибок."""

from fastapi import HTTPException
from starlette.status import (
    HTTP_409_CONFLICT, HTTP_500_INTERNAL_SERVER_ERROR
)


class EmailUniqueHTTPException(HTTPException):
    """Ощибка не уникального эмэйла."""

    def __init__(self):
        """Функция инициализации."""
        super().__init__(
            status_code=HTTP_409_CONFLICT,
            detail={'message': {
                'ru': 'Адрес электронной почты уже зарегистрирован',
                'en': 'Email is already registered'
            }}
        )


class UsernameUniqueHTTPException(HTTPException):
    """Ощибка не уникального юзернэйма."""

    def __init__(self):
        """Функция инициализации."""
        super().__init__(
            status_code=HTTP_409_CONFLICT,
            detail={'message': {
                'ru': 'Пользовательское имя уже зарегистрировано',
                'en': 'Username is already registered'
            }}
        )


class DataBaseHTTPException(HTTPException):
    """Ощибка базы данных."""

    def __init__(self):
        """Функция инициализации."""
        super().__init__(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail={'message': {
                'ru': 'Неизвестная ошибка',
                'en': 'Unknown error'
            }}
        )


class NotFoundByUsernameHTTPException(HTTPException):
    """Ощибка поиска пользователя."""

    def __init__(self):
        """Функция инициализации."""
        super().__init__(
            status_code=HTTP_409_CONFLICT,
            detail={'message': {
                'ru': 'Пользователь с таким именем не найден',
                'en': 'Not found user with this name'
            }}
        )


class WrongPasswordHTTPException(HTTPException):
    """Ощибка не правильного пароля."""

    def __init__(self):
        """Функция инициализации."""
        super().__init__(
            status_code=HTTP_409_CONFLICT,
            detail={'message': {
                'ru': 'Пароль не верный',
                'en': 'Wrong password'
            }}
        )
