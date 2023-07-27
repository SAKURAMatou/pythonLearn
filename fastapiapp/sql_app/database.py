from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 指定数据库地址
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# connect_args={"check_same_thread": False}SQLite 数据库设置的连接参数，它的作用是在单线程环境中禁用检查相同线程。这通常在开发和测试阶段使用。

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 创建数据库会话。数据库会话是与数据库进行交互的主要接口，我们可以使用会话来执行数据库查询、插入、更新和删除等操作。
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# sqlalchemy的表实体的基类
Base = declarative_base()


# 每一个请求有一个独立的数据库会话/连接，在所有请求中使用相同的会话，然后在请求完成后关闭它

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
