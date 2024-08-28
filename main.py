from fastapi import FastAPI
from routes.crud_route import router

app=FastAPI()

app.include_router(router)