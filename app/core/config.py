from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    PG_USER: str
    PG_PASSWORD: str
    PG_SERVER: str
    PG_PORT: str = "5432"
    PG_DB: str

    SQLALCHEMY_DATABASE_URL: PostgresDsn | None = None

    @validator("SQLALCHEMY_DATABASE_URL", pre=True)
    def assemble_db_connection(cls, v: str | None, values: dict[str, str]) -> str:
        """Join DB connection credentials into a connection string"""
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values["PG_USER"],
            password=values["PG_PASSWORD"],
            host=values["PG_SERVER"],
            port=values.get("PORT"),
            path=f"/{values.get('PG_DB') or ''}",
        )

    class Config:
        env_file = ".env"


settings = Settings()
