from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str
    items_per_user: int = 50

    # 读取配置文件需要使用python-dotenv
    class Config:
        env_file = ".env"


# lru_cache让方法执行结果进行缓存，函数只执行一次，后续的执行都是直接从缓存中取值
@lru_cache()
def get_settings():
    return Settings()
