import datetime
import random
import uuid

from bmfwmodels import CnsCinfo
# from models_8 import CnsCinfo
from faker import Faker

from SerialnumGenerate import redisUtils, getSerialnum


class AddCinfo():
    fake = Faker(['zh_cn'])
    redisConnec = redisUtils().r

    def initCinfo(self):
        cinfo = CnsCinfo()
        cinfo.ROWGUID = uuid.uuid4()
        cinfo.RQSTTITLE = self.fake.text(random.randint(10, 50))
        cinfo.rqsttitle = cinfo.RQSTTITLE
        cinfo.RQSTCONTENT = self.fake.text(random.randint(100, 500))
        cinfo.RQSTSOURCE = 'WZ'
        cinfo.RQSTAREACODE = '3205'
        cinfo.AREACODE = '3205'
        cinfo.CSTATUS = '0'
        cinfo.RQSTPERSON = self.fake.name()
        cinfo.LINKNUMBER = self.fake.phone_number()
        cinfo.RQSTNUMBER=cinfo.LINKNUMBER
        cinfo.CLIENGGUID = uuid.uuid4()
        cinfo.RQSTTIME = datetime.datetime.now()
        cinfo.ISSECRET = '0'
        cinfo.ISIMPT = '30'
        cinfo.REPLAYTYPE = '1'
        cinfo.SERIALNUM = cinfo.RQSTSOURCE + datetime.datetime.now().strftime('%Y%m%d') + str(
            random.randint(2000, 3000))
        cinfo.WEBRQSTTIME = cinfo.RQSTTIME
        cinfo.SERIALNUM = getSerialnum(sLen=5, flag=cinfo.RQSTSOURCE)
        return cinfo

    def getCinfoList(self, count):
        res = []
        resSQL = []
        if count is None:
            count = 5

        for i in range(count):
            cinfo = self.initCinfo()
            cinfo.rqsttitle = cinfo.rqsttitle.replace('\n', ';')
            cinfo.RQSTCONTENT = cinfo.RQSTCONTENT.replace('\n', ';')
            res.append(cinfo)
            resSQL.append(getInsertSql(cinfo))

        file = open('insertToCinfo.sql', 'w+', encoding='utf-8')
        try:
            for c in resSQL:
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
    AddCinfo().getCinfoList(5)
