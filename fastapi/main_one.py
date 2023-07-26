from typing import Union

from fastapi import FastAPI, HTTPException, Request, Depends, Header
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
import uvicorn
from pydantic import BaseModel

app = FastAPI()
items = {"foo": "The Foo Wrestlers"}
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# 错误处理，通过HTTPException异常的形式，其中detail入参是请求的返回内容，headers自定义响应的响应头

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found", headers={"X-Error": "There goes my error"})
    return {"item": items[item_id]}


# 自定义异常处理器:UnicornException
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(status_code=418, content={'message': f'全局异常处理返回信息：{exc.name}'})


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


# 依赖注入;提供依赖对象，由框架进行依赖对象的调用，提高复用性
async def common_parameters(q: Union[str, None] = None,
                            skip: int = 0,
                            limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 10):
        self.q = q
        self.skip = skip
        self.limit = limit


# 依赖类的情况下，commons: CommonQueryParams = Depends(CommonQueryParams)可以简写为commons: CommonQueryParams = Depends()
@app.get("/items")
async def read_items(commons: CommonQueryParams = Depends()):
    print(hash(commons))
    return commons


async def verify_token(x_token: str = Header()):
    print("x_token")
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=403, detail="X-Token header invalid")


async def verify_key(x_key: str = Header()):
    print("x_key")
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=403, detail="X-key header invalid")


# 有多个的时候按照dependencies的顺序进行调用依赖项
@app.get("/item/token", dependencies=[Depends(verify_key), Depends(verify_token)])
async def read_items_token():
    return [{"item": "Foo"}, {"item": "Bar"}]


# debug模式启动时，热部署需要把app参数传入导入的字符串，即启动uvicorn的那个字符串
if __name__ == "__main__":
    uvicorn.run(app="main_one:app", host="127.0.0.1", port=8000, reload=True)
