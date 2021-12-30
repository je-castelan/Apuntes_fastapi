from fastapi import FastAPI

from blog.routers import authentication
from blog import models
from blog.database import engine

from blog.routers import blog, user

# Initialize fast api
app = FastAPI()

# Create models automatelly
models.Base.metadata.create_all(engine)

# Routing 
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
