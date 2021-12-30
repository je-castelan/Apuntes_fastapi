from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session

from ..schema import ShowUserSchema, UserSchema

from ..database import get_db

from blog.repository import user as user_repo

# Initialize router
router = APIRouter(
    prefix='/user',
    tags=['Users']
)

#Following are functions

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowUserSchema)
def create_user(
    user: UserSchema,
    db: Session = Depends(get_db)
):
    return user_repo.create(user, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model = ShowUserSchema)
def retrieve_user(
    id: int,
    db: Session = Depends(get_db)
):
    return user_repo.retrieve(id, db)
