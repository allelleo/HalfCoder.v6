from typing import NewType

Model = NewType('Model', object)

async def unique_username(UserModel: Model, username: str) ->bool:
    if await UserModel.exists(username=username):
        return False
    return True


async def unique_email(UserModel: Model, email: str) ->bool:
    if await UserModel.exists(email=email):
        return False
    return True
