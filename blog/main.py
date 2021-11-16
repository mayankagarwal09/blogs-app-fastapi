from fastapi import FastAPI
from blog.models import user
from .database import engine
from .models import blog
from blog import database
from .routers import blog as blogRouter
from .routers import user as userRouter
from .routers import authentication as authRouter


app = FastAPI()

blog.Base.metadata.create_all(bind = engine)
user.Base.metadata.create_all(bind = engine)

get_db = database.get_db

app.include_router(blogRouter.router)
app.include_router(userRouter.router)
app.include_router(authRouter.router)
