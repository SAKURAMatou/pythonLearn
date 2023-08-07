from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')
    app_name: str = "Awesome API"
    admin_email: str
    items_per_user: int = 50
    log_dir_name: str

    # 读取配置文件需要使用python-dotenv
    # class Config:
    #     env_file = ".env"


# lru_cache让方法执行结果进行缓存，函数只执行一次，后续的执行都是直接从缓存中取值
@lru_cache()
def get_settings():
    return Settings()


if __name__ == "__main__":
    print(get_settings())
