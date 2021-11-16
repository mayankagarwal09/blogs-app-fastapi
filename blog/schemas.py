from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    username: str
    password: str

    class Config():
        orm_mode = True

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = False

    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    name: str
    username: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

    class Config():
        orm_mode = True

class TokenData(BaseModel):
    username: Optional[str] = None


