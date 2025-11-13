from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Flashcard, User
from main import get_db
from auth import get_current_user
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import List

router = APIRouter()

class FlashcardBase(BaseModel):
    lesson_id: int
    question: str
    answer: str

class ReviewResponse(BaseModel):
    quality: int  # 0-5, SM-2 quality

@router.get("/flashcards/due")
def get_due_flashcards(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    now = datetime.utcnow()
    flashcards = db.query(Flashcard).filter(
        Flashcard.user_id == current_user.id,
        Flashcard.due_date <= now
    ).all()
    return flashcards

@router.post("/flashcards")
def create_flashcard(flashcard: FlashcardBase, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_flashcard = Flashcard(
        user_id=current_user.id,
        lesson_id=flashcard.lesson_id,
        question=flashcard.question,
        answer=flashcard.answer
    )
    db.add(db_flashcard)
    db.commit()
    db.refresh(db_flashcard)
    return db_flashcard

@router.post("/flashcards/{flashcard_id}/review")
def review_flashcard(flashcard_id: int, review: ReviewResponse, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    flashcard = db.query(Flashcard).filter(
        Flashcard.id == flashcard_id,
        Flashcard.user_id == current_user.id
    ).first()
    if not flashcard:
        raise HTTPException(status_code=404, detail="Flashcard not found")

    # SM-2 Algorithm
    quality = review.quality
    if quality >= 3:
        if flashcard.repetitions == 0:
            interval = 1
        elif flashcard.repetitions == 1:
            interval = 6
        else:
            interval = round(flashcard.interval * flashcard.easiness)
        flashcard.repetitions += 1
    else:
        flashcard.repetitions = 0
        interval = 1

    flashcard.easiness = max(1.3, flashcard.easiness + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)))
    flashcard.interval = interval
    flashcard.due_date = datetime.utcnow() + timedelta(days=interval)

    db.commit()
    return {"message": "Review recorded"}

@router.get("/flashcards")
def get_user_flashcards(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    flashcards = db.query(Flashcard).filter(Flashcard.user_id == current_user.id).all()
    return flashcards
