from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import get_db
from models import Lesson

router = APIRouter()

@router.get("/")
def get_lessons(db: Session = Depends(get_db)):
    lessons = db.query(Lesson).all()
    return [
        {
            "id": lesson.id,
            "title": lesson.title,
            "topic": lesson.topic,
            "description": lesson.description,
            "difficulty": lesson.difficulty,
            "microgames": lesson.microgames
        }
        for lesson in lessons
    ]

@router.get("/{lesson_id}")
def get_lesson(lesson_id: int, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return {
        "id": lesson.id,
        "title": lesson.title,
        "topic": lesson.topic,
        "description": lesson.description,
        "difficulty": lesson.difficulty,
        "microgames": lesson.microgames
    }
