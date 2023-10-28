from fastapi import APIRouter, Depends

from app.adapter.auth.schemas import RegistrationSchema, LoginSchema

from app.adapter.auth.service.login import login
from app.adapter.auth.service.registration import registration as reg_service

controller = APIRouter()


@controller.post('/registration')
async def registration(user: RegistrationSchema):
    return await reg_service(user)


@controller.post('/login')
async def login(user: LoginSchema):
    return await login(user)
