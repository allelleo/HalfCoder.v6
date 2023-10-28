"""Файл с провайдерами."""

import jwt
from .settings import JWTSettings


class Authentication:
    """Класс для авторизации."""

    def __init__(self):
        """Функция инициализации."""
        self.SECRET_KEY = JWTSettings.SECRET_KEY
        self.ALGORITHM = JWTSettings.ALGORITHM

    def login(self, user_id):
        """Функция получения токена."""
        return jwt.encode({'user_id': user_id},
                          self.SECRET_KEY, algorithm=self.ALGORITHM)

    def decode(self, token):
        """Функция декодирования токена."""
        return jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
