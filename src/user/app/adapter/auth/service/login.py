from app.api.v1.models import (
    User
)

from app.adapter.auth.schemas import LoginSchema

from app.api.v1.utils.unique import unique_username, unique_email

import app.adapter.auth.exceptions as E


async def login(model: LoginSchema):
    """Функция для логина пользователя."""
    if await unique_username(User, model.username):
        raise E.NotFoundByUsernameHTTPException
    try:
        user = await User.get(username=model.username)
    except User.DoesNotExist:
        raise E.NotFoundByUsernameHTTPException
    if not await user.check_password(model.password):
        raise E.WrongPasswordHTTPException

    return {
        'user_id': user.id,
    }