from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserCreateResponse, UserLoginResponse
from app.dependencies import get_db, get_current_active_user
from app.crud.user import get_user_by_email, get_user, create_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserCreateResponse)
def register_user(user_in: UserCreate, db_session: Session = Depends(get_db)):
    user = get_user_by_email(db_session, user_in.email)

    if user:
        raise HTTPException(status_code=409, detail=f"Email: {user.email} already in use")

    user = create_user(db_session, user_in)
    return user


@router.get("/me", response_model=UserLoginResponse)
def get_me(db_session: Session = Depends(get_db), current_user: UserLoginResponse = Depends(get_current_active_user)):
    return current_user


@router.get("/{user_id}", response_model=UserLoginResponse)
def read_user(user_id: int, db_session: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    user = get_user(db_session, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="A user with this id does not exist")

    return user
