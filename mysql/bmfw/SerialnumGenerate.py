import redis
import time

redisSetting = {
    "host": "192.168.233.5",
    "port": 6379,
    "db": 1
}
nowTimeStr = time.strftime('%Y%m%d', time.localtime())


def getSerialnum(sLen=5, flag='WZ', redisConnection=None):
    '''订单编号格式'''
    serialnum = f'{flag}{nowTimeStr}'
    formatType = '{:0>' + str(sLen) + 's}'
    # serialnum += formatType.format(45)
    serialnum += formatType.format(getSerialnumCount(redisConnection))
    print(serialnum)
    return serialnum


def getSerialnumCount(redisConnec):
    if redisConnec is None:
        redisConnec = redisUtils().r

    key = f'CnsFS_{nowTimeStr}_服务单号_WZ'
    ser = redisConnec.incrby(key, 1)
    if ser == 1:
        redisConnec.pexpire(key, 86400000)

    ser = str(ser)
    return ser


class redisUtils():
    r = None

    def __init__(self):
        pool = redis.ConnectionPool(host=redisSetting.get("host"), port=redisSetting.get("port"),
                                    db=redisSetting.get("db"))
        self.r = redis.Redis(connection_pool=pool)


if __name__ == '__main__':
    getSerialnum(6)
