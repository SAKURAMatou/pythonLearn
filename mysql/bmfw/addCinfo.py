import datetime
import random
import uuid

from bmfwmodels import CnsCinfo
from faker import Faker

fake = Faker(['zh_cn'])


def initCinfo():
    cinfo = CnsCinfo()
    cinfo.ROWGUID = uuid.uuid4()
    cinfo.rqsttitle = fake.text(random.randint(10, 50))
    cinfo.RQSTCONTENT = fake.text(random.randint(100, 500))
    cinfo.RQSTSOURCE = 'WZ'
    cinfo.RQSTAREACODE = '3205'
    cinfo.CSTATUS = '0'
    cinfo.RQSTPERSON = fake.name()
    cinfo.LINKNUMBER = fake.phone_number()
    cinfo.CLIENGGUID = uuid.uuid4()
    cinfo.RQSTTIME = datetime.datetime.now()
    cinfo.ISSECRET = '0'
    cinfo.ISIMPT = '30'
    cinfo.REPLAYTYPE = '1'
    return cinfo


def getCinfoList(count):
    res = []
    if count is None:
        count = 5

    for i in range(count):
        cinfo = initCinfo()
        res.append(getInsertSql(cinfo))

    file = open('insertToCinfo.sql', 'w+', encoding='utf-8')
    try:
        for c in res:
            file.write(c)
            file.write("\n")
        file.flush()
        print("已生成")
    except Exception as e:
        print(e)
    finally:
        file.close()

    return res


def getInsertSql(cinfo: CnsCinfo):
    k = []
    v = []
    for attr, value in cinfo.__dict__.items():
        if attr == '_sa_instance_state':
            continue
        k.append(attr)
        v.append(str(value))

    k = ",".join(k)
    v = "','".join(v)
    str1 = f"insert into {cinfo.__tablename__}({k}) values('{v}');"
    return str1


if __name__ == '__main__':
    getCinfoList(5)
