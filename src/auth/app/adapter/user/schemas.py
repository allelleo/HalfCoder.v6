from pydantic import BaseModel, EmailStr


class RegistrationSchema(BaseModel):
    """Схема данных для регистрации."""

    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class LoginSchema(BaseModel):
    """Схема данных для логина."""

    username: str
    password: str
