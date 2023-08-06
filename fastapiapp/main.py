import uvicorn
from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from dependencies import get_query_token
from fastapiapp.routers.users import MyException
from routers import items, users
from internal import admin

import logging

logger = logging.getLogger(__name__)

# items和users中都有相同的变量名router，为了避免冲突，通过模块.变量名方式引用

# include_router把 APIRouter 添加到主 FastAPI 应用程序中。
app = FastAPI(debug=True, dependencies=[Depends(get_query_token)])


@app.exception_handler(MyException)
async def unicorn_exception_handler(request: Request, exc: MyException):
    print(f"OMG! An MyException error!: {repr(exc)}")
    logger.error(f"MyException caught in main.py: {exc.des}")
    return JSONResponse(status_code=418, content={'message': f'全局异常处理返回信息：{exc.des}'})


# 在app中使用子模块中的接口
app.include_router(users.router)
app.include_router(items.router)

# 假设admin中的接口时无法被修改的，想要添加项目已有的dependencies，以及接口路径前缀可以把相关信息通过app.include_router()配置
app.include_router(admin.router,
                   prefix="/admin",
                   dependencies=[Depends(get_query_token)],
                   responses={418: {"description": "I'm a teapot"}}, )

from sql_app import models
from sql_app.database import engine

# 根据模型创建数据表
models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    raise MyException(des="Hello Bigger Applications!")
    return {"message": "Hello Bigger Applications!"}


@app.get("/unicorns/{name}")
async def exception_test(name: str = ""):
    if name == "yolo":
        raise MyException(des="Hello Bigger Applications!")
    return {"unicorn_name": name}


if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
