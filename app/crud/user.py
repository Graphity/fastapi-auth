from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password


def get_user(db_session, user_id: int) -> User:
    return db_session.query(User).filter(User.id == user_id).first()


def get_user_by_email(db_session, email: str) -> User:
    return db_session.query(User).filter(User.email == email).first()


def create_user(db_session, user_in: UserCreate) -> User:
    password = hash_password(user_in.password)
    user = User(**user_in.dict(exclude={"password"}), password=password)

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    return user
