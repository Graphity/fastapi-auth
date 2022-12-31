## Example of required environment variables:

```
SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=360

PG_USER=postgres
PG_PASSWORD=
PG_SERVER=localhost
PG_PORT=5432
PG_DB=app

# optional
SQLALCHEMY_DATABASE_URL=postgresql://postgres@localhost:5432/app
```

## Generate `SECRET_KEY`:

```console
$ openssl rand -hex 32
```

## Create `users` table:

```console
cd fastapi-auth
alembic upgrade 693c5ee3969a
```

## Run:

```console
cd fastapi-auth
uvicorn app.main:app --reload
```
