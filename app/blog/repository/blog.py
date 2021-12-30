from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from blog.schema import BlogSchema

from blog import models

def get_all(db: Session):
    blogs = db.query(models.BlogModel).all()
    return blogs

def create(blog: BlogSchema, db: Session):
    new_blog = models.BlogModel(
        title=blog.title,
        body=blog.body,
        user_id = 1
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def retrieve(id: int, db: Session):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Id {id} not found'
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Id {id} not found'}
    return blog

def delete(id: int, db: Session):
    blog = db.query(models.BlogModel).filter(
        models.BlogModel.id == id
    )
    _is_blog_id_exists(blog)
    blog.delete(synchronize_session=False)
    db.commit()

    return "bye"

def update(id: int, request: BlogSchema, db: Session):
    blog = db.query(models.BlogModel).filter(
        models.BlogModel.id == id
    )
    _is_blog_id_exists(blog)
    blog.update(request.dict()) # Fix on tutorial
    db.commit()
    return "updated"


def _is_blog_id_exists(blog):
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Id {id} not found'
        )
