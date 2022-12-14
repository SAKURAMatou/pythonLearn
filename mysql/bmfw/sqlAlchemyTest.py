import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import urllib.parse as urlPase

import addCinfo


def generateEngine(user, password, host, dbname):
    dateBaseUrl = "mysql+pymysql://{user}:{password}@{host}/{dbname}".format(user=user,
                                                                             password=password.replace("@", "%40"),
                                                                             host=host,
                                                                             dbname=dbname)
    dateBaseUrl = "dm+dmPython://{user}:{password}@{host}/{dbname}".format(user=user,
                                                                            password=password.replace("@", "%40"),
                                                                            host=host,
                                                                            dbname=dbname)
    print(dateBaseUrl)
    print(urlPase.quote_plus(dateBaseUrl))
    # engine = create_engine(urllib.parse.quote_plus(dateBaseUrl))
    engine = create_engine(dateBaseUrl)

    # with engine.connect() as conn:
    #     result = conn.execute(text("select 'hello world'"))
    #     print(result.all())

    Session = sessionmaker(engine)
    with Session.begin() as session:
        query = session.query(text("select * from cns_cinfo where rowguid='0ff59240-7299-4e9a-a570-c4736919d95c'"))
        print(query)


    # with Session.begin() as session:
    #     try:
    #         cinfo_list = addCinfo.getCinfoList()
    #         for c in cinfo_list:
    #             session.add(c)
    #         session.commit()
    #     except Exception as e:
    #         print(e)
    #         session.rollback()


if __name__ == "__main__":
    # generateEngine('root', 'Infra5@Gep0int', '192.168.204.180:3306', 'cnsbzb_v9.4kf')
    generateEngine('test1124', '111111111', '192.168.212.203:5236', 'test1124')
