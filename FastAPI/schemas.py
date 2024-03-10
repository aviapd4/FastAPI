from pydantic import BaseModel
from typing import List, Optional

class BookCreate(BaseModel):
    title: str
    author: str
    publication_year: int

class ReviewCreate(BaseModel):
    text: str
    rating: int
    

class BookFilter(BaseModel):
    author: Optional[str] = None
    publication_year: Optional[int] = None

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    publication_year: int
    reviews: List[ReviewCreate]
