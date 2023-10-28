from app.adapter.user.service.api import APIClient, APIProcess
from app.adapter.user.schemas import RegistrationSchema, LoginSchema
from app.providers import Authentication

from fastapi import APIRouter

controller = APIRouter()


@controller.post('/registration')
async def registration(user: RegistrationSchema):
    print(1)
    return await APIProcess.registration(await APIClient.call_registration(user=user))


@controller.post('/login')
async def login(user: LoginSchema):
    return await APIProcess.login(await APIClient.call_login(user=user), Authentication())

