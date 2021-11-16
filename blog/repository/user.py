from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from ..models.user import User
from .. import schemas
from ..utils.hashing import Hashing


def create(user: schemas.User, db: Session):
    hashed_pswd = Hashing.get_hashed_password(user.password)
    new_user = User(name= user.name, username = user.username, password= hashed_pswd)
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        if e.__class__.__name__ == "IntegrityError":
            raise HTTPException(status_code= status.HTTP_422_UNPROCESSABLE_ENTITY, detail="username already taken")
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail='something went wrong')

def get(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="user with given username not found")
    return user