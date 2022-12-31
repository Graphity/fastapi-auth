from fastapi import FastAPI

from . import models
from .routers import auth, users
from .database import engine

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)

models.Base.metadata.create_all(bind=engine)
