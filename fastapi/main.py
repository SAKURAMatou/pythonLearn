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


# 响应输出模型：接收的类型与 Pydantic 模型属性所声明的类型相同，因此它可以是一个 Pydantic 模型，但也可以是一个由 Pydantic 模型组成的 list，例如 List[Item]。
# 响应输出模型作用：1、将输出数据转换为其声明的类型,2、校验数据，3、在api文档中展示

# 定义输入，输出的模型对象
class UserIn(BaseModel):
    username: str
    password: str
    email: str
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: str
    full_name: Union[str, None] = None


# 不指定响应模型时，将返回和输入一样的模型，指定时，转化为输出模型
# response_model_exclude_unset忽略响应模型中的默认空值；full_name默认空，当不设置时也会返回，设置时，为空则从返回字段中删除空值字段
@app.post("/users/create", response_model=UserOut, response_model_exclude_unset=True, response_model_include={'email'})
def create_user(user: UserIn):
    return user


# response_model_include 和 response_model_exclude接收由属性名称 str 组成的 set 进行忽略/指定特定返回字段操作
# response_model除了是pydantic模型之外还可以是List[Item]，多个模型中的任意一个，任意的dict
# from typing import Dict,List,Union
# response_model=Dict[str, float]；response_model=Union[PlaneItem, CarItem]； response_model=Dict[str, float]


# 表单请求
# 需要先安装python-multipart： pip install python-multipart
from fastapi import Form


# 使用 Form 可以声明与 Body （及 Query、Path、Cookie）相同的元数据和验证
@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    print(username, password)
    return {"username": username}


# 文件上传
from fastapi import UploadFile, File


# 单个文件上传时接口入参名称和请求时文件的名称一致
# 指定非必填 file: Union[UploadFile, None] = None或file: UploadFile = File(default=None)
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(default=None, description="A file read as UploadFile"),
                             username: str = Form(),
                             password: str = Form()):
    if file:
        return {"filename": file.filename, "username": username}
    else:
        return {"username": username}


# 多个文件上传时，指定入参类型是List[UploadFile];是一个参数files中包含多个文件对象
@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}

# UploadFile 接收文件优势：
# 使用 spooled 文件；存储在内存的文件超出最大上限时，FastAPI 会把文件存入磁盘
# 更适于处理图像、视频、二进制文件等大型文件，好处是不会占用所有内存
# 获取上传文件的元数据
# 自带file-like接口，（file-like object -- 文件类对象，python的文件对象）

# UploadFile 的属性如下：
#
# filename：上传文件名字符串（str），例如， myimage.jpg；
# content_type：内容类型（MIME 类型 / 媒体类型）字符串（str），例如，image/jpeg；
# file： SpooledTemporaryFile（ file-like 对象）。其实就是 Python文件，可直接传递给其他预期 file-like 对象的函数或支持库。
# UploadFile 支持以下 async 方法，（使用内部 SpooledTemporaryFile）可调用相应的文件方法。
#
# write(data)：把 data （str 或 bytes）写入文件；
# read(size)：按指定数量的字节或字符（size (int)）读取文件内容；
# seek(offset)：移动至文件 offset （int）字节处的位置；
# 例如，await myfile.seek(0) 移动到文件开头；
# 执行 await myfile.read() 后，需再次读取已读取内容时，这种方法特别好用；
# close()：关闭文件。
# 因为上述方法都是 async 方法，要搭配「await」使用。
