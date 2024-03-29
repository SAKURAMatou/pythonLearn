from typing import Optional, Union

from pydantic import BaseModel
from sqlalchemy import String, Boolean, Float, Text, ForeignKey, Column, select, and_, Select, func, desc, asc, inspect
from datetime import datetime
from typing import Any
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, as_declarative


class ResumeSendBasic(BaseModel):
    cname: Optional[str] = None
    mguid: Optional[str] = None
    salary: Optional[float] = None
    heartlevel: Optional[str] = None
    cwebsite: Optional[str] = None
    jobdescription: Optional[str] = None
    jobname: Optional[str] = None
    requirement: Optional[str] = None
    comment: Optional[str] = None
    guid: Optional[str] = None
    userguid: Union[str, None] = None
    cpage: Optional[int] = 1
    pagesize: Optional[int] = 10


@as_declarative()
class ConditionMixin:
    _like_conditions: list[{}] = []
    _less_conditions: list[{}] = []
    _great_conditions: list[{}] = []
    _equal_conditions: list[{}] = []

    def equal(self, columns, value):
        self._equal_conditions.append({columns: value})


class Base(DeclarativeBase):
    pass


class BaseChild(DeclarativeBase):

    def __init__(self, **kw: Any):
        super().__init__()
        for key, value in kw.items():
            setattr(self, key, value)
        self._like_conditions: list[{}] = []
        self._less_conditions: list[{}] = []
        self._great_conditions: list[{}] = []
        self._equal_conditions: list[{}] = []

    def equal(self, columns, value):
        self._equal_conditions.append({columns: value})

    def less(self, columns, value):
        self._less_conditions.append({columns: value})

    def great(self, columns, value):
        self._great_conditions.append({columns: value})

    def like(self, columns, value: str):
        if not (value.startswith('%') and value.endswith('%')):
            self._like_conditions.append({columns: f'%{value}%'})
        else:
            self._like_conditions.append({columns: value})

    def to_dict(self):
        """ROM转dict，排除空值"""
        data = {}
        for c in self.__table__.columns:
            v = getattr(self, c.name)
            if v is not None:
                data[c.name] = v
        return data

    def to_dict_all(self):
        """ORM转dict，全字段"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_columns(cls):
        inspector = inspect(cls)
        return [column.key for column in inspector.attrs]

    def where_condition(self) -> list:
        conditions = []
        columns = self.__table__.columns
        if len(self._equal_conditions) > 0:
            for i in self._equal_conditions:
                for key, value in i.items():
                    conditions.append(columns[key] == value)
        if len(self._less_conditions) > 0:
            for i in self._less_conditions:
                for key, value in i.items():
                    conditions.append(columns[key] < value)
        if len(self._great_conditions) > 0:
            for i in self._great_conditions:
                for key, value in i.items():
                    conditions.append(columns[key] > value)
        if len(self._like_conditions) > 0:
            for i in self._like_conditions:
                for key, value in i.items():
                    conditions.append(columns[key].like(value))
        return conditions

    def get_sql_select(self, *selectFields) -> Select:
        """查询count时传入对应的count，例如func.count("*").label("count")"""
        if not selectFields:
            columns = self.__table__.columns
        # 获取搜索条件列表
        conditions = self.where_condition()
        if len(conditions) == 0:
            return select(*columns)
        return select(*columns).where(and_(*self.where_condition()))

    def get_sql_list(self, *selectFields, currentPage=1, pagesize=10, orderby=None, order='desc') -> Select:
        """分页查询数据；默认值：currentPage=1, pagesize=10, order='desc'"""
        if not selectFields:
            columns = self.__table__.columns
        # 获取搜索条件列表
        conditions = self.where_condition()
        sql = select(*columns)
        if len(conditions) > 0:
            sql = sql.where(and_(*self.where_condition()))
        if orderby:
            if 'desc' == order:
                sql = sql.order_by(desc(orderby))
            else:
                sql = sql.order_by(asc(orderby))
        if all([currentPage, pagesize]):
            sql = sql.limit(pagesize).offset((currentPage - 1) * pagesize)

        return sql

    @classmethod
    def get_cls(cls):
        print(select(cls))

    def get_from_cls(self):
        self.get_cls()

    pass


class ResumeSend(BaseChild):
    __tablename__ = 'dml_resume_send'
    rowguid: Mapped[str] = mapped_column(String(50), primary_key=True)
    # mguid: Mapped[str] = mapped_column(String(50))
    cname: Mapped[str] = mapped_column(String(20))
    jobname: Mapped[str] = mapped_column(String(20))
    salary: Mapped[float] = mapped_column(Float(precision=1))
    sendtime: Mapped[datetime] = mapped_column(default=datetime.now)
    cwebsite: Mapped[str] = mapped_column(String(100), default=None, nullable=True)
    heartlevel: Mapped[str] = mapped_column(String(1), default='3')
    jobdescription: Mapped[str] = mapped_column(Text, default=None, nullable=True)
    requirement: Mapped[str] = mapped_column(Text, default=None, nullable=True)
    comment: Mapped[str] = mapped_column(Text, default=None, nullable=True)
    mguid = Column(String(50), ForeignKey("dml_job_search.rowguid"))
    userguid: Mapped[str] = mapped_column(String(50))
    isdel: Mapped[bool] = mapped_column(Boolean, default=False)
