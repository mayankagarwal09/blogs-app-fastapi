from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from blog import schemas
from ..database import get_db
from ..models.user import User
from ..utils.hashing import Hashing
from ..repository import user as userRepository


router = APIRouter(tags=['Users'])

@router.post('/users', status_code= status.HTTP_201_CREATED)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return userRepository.create(user, db)

@router.get('/users/{username}', response_model=schemas.ShowUser)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    return userRepository.get(username, db)