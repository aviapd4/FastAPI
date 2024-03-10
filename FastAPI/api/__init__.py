from fastapi import APIRouter

router = APIRouter()

# Import other route modules here
from . import books, reviews
