from fastapi.testclient import TestClient
from main import app
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Book
import pytest
from database import get_db

# Create all tables in the database before testing
Base.metadata.create_all(bind=engine)

# Override the database dependency to use a test session
app.dependency_overrides[get_db] = lambda: SessionLocal()

client = TestClient(app)

# Test data
test_book_data = {"title": "Test Book", "author": "Test Author", "publication_year": 2022}
test_review_data = {"text": "Test Review", "rating": 5}

@pytest.fixture
def session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def test_create_book(session: Session):
    response = client.post("/books/", json=test_book_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == test_book_data["title"]
    assert data["author"] == test_book_data["author"]
    assert data["publication_year"] == test_book_data["publication_year"]
    assert "id" in data
    # Clean up after the test
    session.query(Book).filter_by(id=data["id"]).delete()
    session.commit()

def test_get_books(session: Session):
    # Add a test book
    session.add(Book(**test_book_data))
    session.commit()
    response = client.get("/books/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == test_book_data["title"]
    assert data[0]["author"] == test_book_data["author"]
    assert data[0]["publication_year"] == test_book_data["publication_year"]
    # Clean up after the test
    session.query(Book).filter_by(**test_book_data).delete()
    session.commit()
