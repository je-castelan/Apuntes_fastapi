from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session

from blog.oauth2 import get_current_user
from blog.repository import blog as blog_repo

from ..schema import BlogSchema, ShowBlogSchema, UserSchema
from ..database import get_db

# Initialize router
router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


#Following are functions

@router.get('/', response_model = List[ShowBlogSchema])
def all(
    db: Session = Depends(get_db),
    current_user: UserSchema = Depends(get_current_user)
):
    return blog_repo.get_all(db)



@router.post('/', status_code=status.HTTP_201_CREATED)
def create(
    blog: BlogSchema,
    db: Session = Depends(get_db),
    current_user: UserSchema = Depends(get_current_user)
):
    return blog_repo.create(blog, db)



@router.get('/{id}', status_code=status.HTTP_200_OK, response_model = ShowBlogSchema)
def retrieve(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserSchema = Depends(get_current_user)
):
    return blog_repo.retrieve(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserSchema = Depends(get_current_user)
):
    return blog_repo.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int,
    request: BlogSchema,
    db: Session = Depends(get_db),
    current_user: UserSchema = Depends(get_current_user)
):
    return blog_repo.update(id, request, db)
