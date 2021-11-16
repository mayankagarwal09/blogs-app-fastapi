from datetime import datetime, timedelta
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from blog import schemas
from ..database import get_db
from ..repository import auth as authRepository
from fastapi.security import  OAuth2PasswordRequestForm


router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(login: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return authRepository.login(login, db)
