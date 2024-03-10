# FastAPI
Project to create book and review it

# FastAPI Book Review System

This is a FastAPI-based RESTful API for a book review system. Users can add books, submit reviews for books, and retrieve book information and reviews.

## Project Structure

The project consists of the following components:

- `api/`: Contains modules for API route definitions.
  - `books.py`: Defines API routes related to books.
  - `reviews.py`: Defines API routes related to reviews.
- `database.py`: Initializes the database connection and session.
- `crud.py`: Implements CRUD operations for interacting with the database.
- `main.py`: Entry point for the FastAPI application.
- `models.py`: Defines SQLAlchemy models for database tables.
- `schemas.py`: Defines Pydantic models for request/response data validation.
- `tests/`: Contains unit tests for the API endpoints.

## Setup and Installation

1. Clone the repository:


2. Install dependencies:
   pip install -r requirements.txt

## Running the Application

3. To run the FastAPI application, execute the following command:
   uvicorn main:app --reload

This will start the server, and you can access the API endpoints at `http://127.0.0.1:8000`.

## Testing

4. To run unit tests for the API endpoints, execute the following command:
 pytest

This will discover and execute all test functions in the `tests` directory.

## API Documentation

Once the server is running, you can access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

## Background Task

A background task is implemented for sending a confirmation email (simulated) after a review is posted. The email sending task is enqueued asynchronously using FastAPI's background tasks feature. just uncomment the function



   




