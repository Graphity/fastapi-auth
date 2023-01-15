from sqlalchemy import Column, Integer, String, Date, LargeBinary, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(50), nullable=False)
    username = Column(String(32), unique=True, nullable=False, index=True)
    dob = Column(Date, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(LargeBinary, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=func.now())
