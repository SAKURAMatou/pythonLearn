import redis
import time

redisSetting = {
    "host": "localhost",
    "port": 6379,
    "db": 0
}
pool = redis.ConnectionPool(host=redisSetting.get("host"), port=redisSetting.get("port"), db=redisSetting.get("db"))
r = redis.Redis(connection_pool=pool)

