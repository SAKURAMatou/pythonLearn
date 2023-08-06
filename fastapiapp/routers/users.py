from fastapi import APIRouter, Depends, Request

# APIRouter的实例对象等效于FastAPI的实例对象
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

# from fastapiapp.dependencies import MyException
from fastapiapp.sql_app import schema, crud
from fastapiapp.sql_app.database import get_db
import logging

router = APIRouter(prefix="/user")
logger = logging.getLogger(__name__)
class MyException(Exception):
    def __init__(self, des: str):
        self.des = des

# @router.exception_handler(MyException)
# async def unicorn_exception_handler(request: Request, exc: MyException):
#     logger.error(f"MyException caught in user.py: {exc}")
#     return JSONResponse(status_code=418, content={'message': f'全局异常处理返回信息：{exc.des}'})


@router.get("/all", response_model=list[schema.User])
async def read_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    users = crud.get_users(db, skip, limit)
    return users
    # return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/email/{email}", response_model=schema.User)
async def read_user_me(email: str, db: Session = Depends(get_db)):
    by_email = crud.get_user_by_email(db, email)
    return by_email


@router.post("/create/", response_model=schema.User)
async def read_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    """新增用户"""
    email = crud.get_user_by_email(db, user.email)
    if email:
        raise MyException(des="Hello Bigger Applications!")
        # raise MyException(des="Email already registered")
    return crud.create_user(db=db, user=user)
