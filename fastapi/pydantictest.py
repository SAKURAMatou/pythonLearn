from typing import Union

from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    username: str
    password: str
    email: str
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: str
    full_name: Union[str, None] = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: str
    full_name: Union[str, None] = None


# 多个模型时的相关操作
# .dict()是pydantic模型的方法，作用是把pydantic模型转化为一个字典dict

userIn = UserIn(username="test", password="123456", email="test@qq.com")
print(userIn.dict())

# **{} 是python的操作对一个dict对象进行解包，
# UserInDB(**userIn.dict())即用userIn创建一个UserInDB对象，通过pydantic模型转dict+自动解包构成关键字传参创建新的对象
# 在操作多个有相似字段的数据模型时可以减少重复代码
print(UserInDB(**userIn.dict(), hashed_password="*****"))

