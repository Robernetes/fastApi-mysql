from fastapi import APIRouter, Response, status
from config.db import db_conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()


@user.get("/users", response_model=list[User])
def get_users():
    return db_conn.execute(users.select()).fetchall()


@user.post("/users", response_model=User)
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email, "password": f.encrypt(user.password.encode("utf-8"))}
    result = db_conn.execute(users.insert().values(new_user))
    return db_conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get("/users/{id}", response_model=User)
def get_user(id: str):
    return db_conn.execute(users.select().where(users.c.id == id)).first()


@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: str):
    db_conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@user.put("/users/{id}", response_model=User)
def update_user(id: str, user: User):
    db_conn.execute(users.update().values(name=user.name, email=user.email, password=f.encrypt(user.password.encode("utf-8"))).where(users.c.id == id))
    return "updated"
