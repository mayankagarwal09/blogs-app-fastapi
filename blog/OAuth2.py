from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .repository import auth as authRepository
from .repository import user as userRepository
from sqlalchemy.orm import Session
from .database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = authRepository.verify(token, credentials_exception)
    user = userRepository.get(token_data.username, db)
    if user is None:
        raise credentials_exception
    return user