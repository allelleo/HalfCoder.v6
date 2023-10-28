"""Файл конфигурации."""


class AdapterSettings:
    user_service_url = 'http://127.0.0.1:8000/'


class JWTSettings:
    SECRET_KEY = '123'
    ALGORITHM = 'HS256'
