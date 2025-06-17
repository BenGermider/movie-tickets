from fastapi import FastAPI
from routes.movies import router as movies_router
from routes.seats import router as seats_router
app = FastAPI()


app.include_router(movies_router, prefix="/movies")
app.include_router(seats_router, prefix="/seats")
