from sqlalchemy.orm import Session
from models import Book, Review
from schemas import BookCreate, ReviewCreate, BookFilter

def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def create_review(db: Session, book_id: int, review: ReviewCreate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_review = Review(**review.dict(), book_id=book_id)
    db.add(db_review)
    db.commit()
    return {"message": "Review created successfully"}

def get_books(db: Session, filter: BookFilter):
    query = db.query(Book)
    if filter.author:
        query = query.filter(Book.author == filter.author)
    if filter.publication_year:
        query = query.filter(Book.publication_year == filter.publication_year)
    return query.all()
