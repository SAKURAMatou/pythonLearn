from fastapi import FastAPI, Body
from enum import Enum
from typing import Union, List
from pydantic import BaseModel, Required

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 路径参数
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}


# 定义的接口顺序:两个接口/users/me和/users/{user_id}请求/users/me时，如果/users/me定义在/users/{user_id}前，则执行/users/me
# 否则执行/users/{user_id}
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# 通过枚举类指定入参的范围，不在给定枚举的请求会返回异常
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name == ModelName.resnet:
        return {"model_name": model_name, "message": "LeCNN all the images"}
    if model_name == ModelName.lenet:
        return {"model_name": model_name, "message": "Have some residuals"}
    else:
        raise ValueError(f"Invalid model name: {model_name}")


# 请求的入参是url格式默认不识别，可以通过标识为path类型入参;请求/files/home/johndoe/myfile.txt时，/home/johndoe/myfile.txt作为入参而不是路径
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# 请求体入参额外校验


# 查询参数；即不是路径参数，通过url?a=1&b=2&c=3拼接的参数
# 和路径参数一样，查询参数也是 URL 的一部分，因此它们的"原始值"是字符串。
# 和路径参数不同，查询参数是非必填，可以设置默认值
@app.get("/query")
async def query(q: str = "default", page: int = 0):
    return {"q": q, "page": page}


# 默认值为none；可选参数;q的类型指定为str或空，默认值为空
@app.get("/query/default")
async def read_item(q: Union[str, None] = None, page: int = 0):
    return {"q": q, "page": page}


# 通过fastapi的Query给入参添加额外的校验
from fastapi import Query


# Query的default=Required说明参数必填，pydantic中的Required
@app.get("/query/check")
def extra_check(q: Union[str, None] = Query(default=Required, max_length=50, title="q title test",
                                            description="q description test"), page: int = 0):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 查询参数是一个list情况;alias指定别名，值为url中从入参key，指定之后使用pyton接口中指定的入参名称取法获取到数据，需要再url中使用item-query
# 总结，Query有：校验用：alias，min_length，max_length，regex，default，api文档用：title，description
@app.get("/query/list")
def list_with_check(l: List[str] = Query(default=['test', 'list'], alias="item-query")):
    query_items = {"list": l}
    return query_items


# 必填参数，不设置默认值即可，如果参数没有传值，则会报错；即有默认值认为是非必填，否则必填

# 请求体参数，用于非get请求;需要有对应的请求体对象

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.post("/bodyparam")
async def bodyparam(item: Item):
    return {"res": item.dict()}


# 多个请求体入参
class User(BaseModel):
    username: str
    password: str
    full_name: str


# 多个请求体入参相当于对入参JSON做了最外层解析，每个入参对应请求体内的一个子json；入参的item，user是入参json的一层的key
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     },
#     "user": {
#         "username": "dave",
#         "full_name": "Dave Grohl",
#         "password": "fsdafjklhafdshf"
#     }
# }
@app.post("/bodyparams")
def bodyparams(item: Item, user: User):
    return {"res": {"item": item, "user": user}}


# fast api 默认单一的key是查询参数，如果需要指定为请求体参数时需要通过importance: int = Body()
# {"importance":1,"item": {},"user": {}}格式的请求体入参的话
@app.post("/bodyparams/importance")
def bodyparam(item: Item, user: User, importance: int = Body(default=1)):
    return {"res": {"item": item, "user": user, "importance": importance}}


# 单个对象的请求体参数，包含key;
# 入参应该是{"item": {"name": "Foo", "description": "The pretender","price": 42.0,  "tax": 3.2  }}；相比没有指定Body(embed=True)区别在于
# {"name": "Foo", "description": "The pretender","price": 42.0,  "tax": 3.2  }，入参json是否包含入参item这一层封装
@app.post("/bodyparams/embed")
def bodyparams_embed(item: Item = Body(embed=True)):
    return {"res": item}


from pydantic import Field


# 类似于Query Path 请求体参数也可以通过pydantic的Field对字段进行额外校验，用法一致
class BodyWithCheck(BaseModel):
    name: str
    description: str = Field(default=None, max_length=300, min_length=5)
    price: float = Field(ge=2.0)
    tax: Union[float, None] = None


@app.post("/bodywithcheck")
def body_with_check(bodyp: BodyWithCheck):
    return {"res": bodyp}


# Cookie参数 Header参数，和Field，Query Path的用法一样
from fastapi import Cookie, Header


# 大多数标准的headers用 "连字符" 分隔，也称为 "减号" (-)。但是像 user-agent 这样的变量在Python中是无效的。
# 因此, 默认情况下, Header 将把参数名称的字符从下划线 (_) 转换为连字符 (-) 来提取并记录 headers.
# 同时，HTTP headers 是大小写不敏感的，因此，因此可以使用标准Python样式(也称为 "snake_case")声明它们。

@app.post("/headtest")
async def read_items(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent": user_agent}
