from fastapi import APIRouter, Depends, HTTPException

# APIRouter的实例对象等效于FastAPI的实例对象
from sqlalchemy.orm import Session

from fastapiapp.dependencies import MyException
from fastapiapp.sql_app import schema, crud
from fastapiapp.sql_app.database import get_db

router = APIRouter(prefix="/user")


@router.get("/all", response_model=list[schema.User])
def read_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    users = crud.get_users(db, skip, limit)
    return users
    # return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/email/{email}", response_model=schema.User)
def read_user_me(email: str, db: Session = Depends(get_db)):
    by_email = crud.get_user_by_email(db, email)
    return by_email


@router.post("/create/", response_model=schema.User)
def read_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    """新增用户"""
    email = crud.get_user_by_email(db, user.email)
    if email:
        raise MyException(des="Email already registered")
    return crud.create_user(db=db, user=user)
