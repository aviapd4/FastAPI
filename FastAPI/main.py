
from api import books, reviews

from fastapi import FastAPI, Depends
import models
from database import engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(books.router)
app.include_router(reviews.router)
