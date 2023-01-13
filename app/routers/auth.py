from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas.token import Token
from app.dependencies import get_db
from app.crud.user import get_by_email
from app.core.security import create_access_token, check_password

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=Token)
def login_user(user_credentials: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(get_db)):
    user = get_by_email(db_session, user_credentials.username)

    if not user:
        raise HTTPException(status_code=403, detail="Invalid Email")

    if not check_password(user_credentials.password, user.password):
        raise HTTPException(status_code=403, detail="Invalid Password")

    access_token = create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}
