from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.token import Token
from app.schemas.user import UserCreate, UserLoginResponse, UserOut
from app.dependencies import get_db, get_current_active_user
from app.crud.user import get_by_email, get_by_username, create
from app.core.security import create_access_token

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=Token)
def create_user(user_in: UserCreate, db_session: Session = Depends(get_db)):
    user = get_by_email(db_session, user_in.email)

    if user:
        raise HTTPException(status_code=409, detail=f"Email: {user.email} already in use")

    user = create(db_session, user_in)
    access_token = create_access_token(data={"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserLoginResponse)
def get_me(db_session: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/{username}", response_model=UserOut)
def get_user(username: str, db_session: Session = Depends(get_db)):
    user = get_by_username(db_session, username)

    if not user:
        raise HTTPException(status_code=404, detail="A user with this username does not exist")

    return user
