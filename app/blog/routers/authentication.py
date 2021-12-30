from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from blog.repository import authentication
from blog.schema import TokenSchema

from ..database import get_db

router = APIRouter(
    prefix='/login',
    tags=['Authentication']
)

@router.post('/', status_code=status.HTTP_200_OK, response_model=TokenSchema)
def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return authentication.login(request, db)