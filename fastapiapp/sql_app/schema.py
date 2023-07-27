"""
pydantic模型；orm框架使用sqlalchemy，和pydantic的数据模型不一样，
"""
from typing import Union

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    """返回数据的item模型"""
    id: int
    owner_id: int

    # 告诉pydantic当前模型是orm模型；Pydantic模型与 ORM 兼容
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    """返回数据的user模型"""
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
