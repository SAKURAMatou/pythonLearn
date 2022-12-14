import pymysql.cursors
import argparse

parser = argparse.ArgumentParser(description='ArgUtils')
parser.add_argument('-host', type=str, default='localhost', help="data date")
parser.add_argument('-username', type=str, default="root",
                    help="agent_id_from_platform id")
parser.add_argument('-password', type=str, default="11111")
parser.add_argument('db', type=str)
args = parser.parse_args()


def deleteOld(host, username, password, db):
    # connection = pymysql.connect(host='192.168.212.24',
    #                              user='root',
    #                              password='Gepoint',
    #                              database='cnsbzb_v9.1_cs',
    #                              cursorclass=pymysql.cursors.DictCursor)
    connection = pymysql.connect(host=host, user=username, password=password, db=db, charset="UTF-8",
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        if connection is not None:
            cursor = connection.cursor()
            sql = 'select mc.CLIENTIDENTIFIER from cns_warn_supvs c left join messages_center mc on mc.CLIENTIDENTIFIER =c.CLIENTIDENTIFIER  where mc.MESSAGEITEMGUID is not null'
            cursor.execute(sql)
            fetchall = cursor.fetchall()
            deleteCenter = "delete from messages_center where CLIENTIDENTIFIER=%s"
            deletemessage = "delete from messages_message where CLIENTIDENTIFIER=%s"

            print(f"共需要删除数据{len(fetchall)}条")
            for i in fetchall:
                # print(i.get("CLIENTIDENTIFIER"))
                cursor.execute(deleteCenter, (i.get("CLIENTIDENTIFIER")))
                cursor.execute(deletemessage, (i.get("CLIENTIDENTIFIER")))
                # print("deleteres", deleteres)

            # 关闭连接

            cursor.close()
        else:
            print("数据库连接失败！")

    except  Exception as e:
        print(e)
    finally:
        if connection is not None:
            connection.commit()
            connection.close()


if __name__ == '__main__':
    if args is not None:
        # print('testArg',type(args),args)
        # print(args.host, args.username, args.password, args.db)
        if not all(args.host, args.username, args.password, args.db):
            print("确实必要参数！")
        else:
            deleteOld(args.host, args.username, args.password, args.db)
