from fastapi import FastAPI

app = FastAPI(title='HalfCoder User MicroService')

from app.api.v1.controller import controller as v1_controller

app.include_router(v1_controller, prefix='/api/v1/user', tags=['user'])

from app.adapter.adapters import auth_controller

app.include_router(auth_controller, prefix='/api/v1/adapter/auth', tags=['auth', 'adapter'])

from app.database import init

init(app)  # Initialize database

from fastapi.middleware.cors import CORSMiddleware


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)