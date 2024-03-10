from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import ReviewCreate
from database import get_db
from crud import create_review as create_review_db
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine



import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import BackgroundTasks, FastAPI
from pydantic import BaseModel




def send_email(receiver_email: str, review_text: str):
    # Configure email settings
    sender_email = "admin@gmail.com"
    password = "admin"
    
    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Review Confirmation"
    message.attach(MIMEText(f"Thank you for your review:\n\n{review_text}", "plain"))

    # Connect to SMTP server and send email
    with smtplib.SMTP("'smtp.gmail.com'", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())



# Database session
router = APIRouter()
@router.post("/books/{book_id}/reviews/")
def create_review(book_id: int,email:str, review: ReviewCreate,db: Session = Depends(get_db)):
    review_email = email
    
    # Enqueue background task to send email
    #send_email(review_email, review.text)
    return create_review_db(db=db, book_id=book_id, review=review)
