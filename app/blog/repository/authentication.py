from fastapi import status, HTTPException

from blog import models, jwt_token
from blog.security import Hash
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm.session import Session

def login(request: OAuth2PasswordRequestForm, db: Session):
    user = db.query(models.UserModel).filter(
        models.UserModel.email == request.username
    ).first()
    if not user or not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f'Invalid user'
        )
    access_token = jwt_token.create_access_token(
        data={"sub": user.email},
    )
    return {"access_token": access_token, "token_type": "bearer"}
