from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import BookCreate, BookResponse, BookFilter
from database import get_db
from crud import create_book as create_book_db, get_books as get_books_db

router = APIRouter()

@router.post("/books/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book_db(db=db, book=book)

@router.get("/books/", response_model=list[BookResponse])
def get_books(filter: BookFilter = Depends(), db: Session = Depends(get_db)):
    return get_books_db(db=db, filter=filter)
