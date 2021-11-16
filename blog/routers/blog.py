from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from blog import schemas
from ..database import get_db
from ..repository import blog as blogRepository
from ..OAuth2 import get_current_user


router = APIRouter(prefix='/blogs',
                    tags=['Blogs'])

@router.get("/", response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blogRepository.get_all(db, current_user)

@router.post('/', status_code= status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blogRepository.create(blog, db)


@router.get("/{blog_id}", response_model=schemas.ShowBlog)
def get_blog(blog_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blogRepository.get(blog_id, db)

@router.put("/{blog_id}", status_code= status.HTTP_202_ACCEPTED)
def update_blog(blog_id: int, blog: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blogRepository.update(blog_id, blog, db)

@router.delete("/{blog_id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blogRepository.delete(blog_id, db)
