from fastapi import HTTPException, status

from sqlalchemy.orm.session import Session
from blog.schema import UserSchema
from blog import models
from blog.security import Hash

def create(user: UserSchema, db: Session):
    new_user = models.UserModel(
        name=user.name,
        email=user.email,
        password=Hash.bcrypt(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def retrieve(id: int, db: Session):
    user = db.query(models.UserModel).filter(models.UserModel.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User {id} not found'
        )
    return user
