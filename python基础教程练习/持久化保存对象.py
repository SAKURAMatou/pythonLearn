import shelve


def main():
    datab = shelve.open("../data/person.data")
    try:
        while True:
            comment = get_comment()
            if comment == '1':
                look_for(datab)
            elif comment == "2":
                save_person(datab)
    except:
        print("发送异常")
    finally:
        datab.close()


def get_comment():
    print("1:查询\n2:输入")
    return input("输入命令：")


def look_for(db):
    id = input("输入编号：")
    print(f"查询结果：{db[id]}")


def save_person(db):
    pid = input("请输入id：")
    name = input("请输入名字：")
    age = input("请输入年龄：")
    person = {'name': name, 'age': age}
    db[pid] = person


if __name__ == "__main__":
    main()
