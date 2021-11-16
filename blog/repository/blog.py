from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from ..models.blog import Blog
from .. import schemas


def get_all(db: Session, user: schemas.User):
    blogs = db.query(Blog).filter(Blog.username == user.username).all()
    return blogs

def create(blog: schemas.Blog, db: Session):
    new_blog = Blog(title = blog.title, body = blog.body, username= "user1")
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get(blog_id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="no blog with given id found")
    return blog

def delete(blog_id: int, db: Session):
    db.query(Blog).filter(Blog.id == blog_id).delete(synchronize_session= False)
    db.commit()
    return 'deleted'

def update(blog_id: int, blog: schemas.Blog, db: Session):
    blog = db.query(Blog).filter(Blog.id == blog_id).update(blog.dict())
    db.commit()
    return 'updated'