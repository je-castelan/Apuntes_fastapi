from typing import List, Optional
from pydantic import BaseModel

class BlogSchema(BaseModel):
    title: str
    body: str


class OutputBlogSchema(BlogSchema):
    class Config():
        orm_mode = True


class UserSchema(BaseModel):
    name: str
    email: str
    password: str


class ShowUserSchema(BaseModel):
    name: str
    email: str
    blogs: List[OutputBlogSchema] = []

    class Config():
        orm_mode = True


class ShowBlogSchema(BaseModel):
    title: str
    body: str
    creator: ShowUserSchema
    class Config():
        orm_mode = True


class LoginSchema(BaseModel):
    username: str
    password: str

class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None