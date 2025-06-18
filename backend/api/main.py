from fastapi import FastAPI
from .routes import (
    movies_router,
    seats_router
)
app = FastAPI()


app.include_router(movies_router)
app.include_router(seats_router)
