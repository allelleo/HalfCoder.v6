from fastapi import FastAPI

app = FastAPI(title='HalfCoder Auth MicroService')

from .adapter.adapters import controller as adapter

app.include_router(adapter, tags=['auth', 'call adapters'])