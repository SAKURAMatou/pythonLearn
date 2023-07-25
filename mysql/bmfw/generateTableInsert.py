import random
import string

# 表结构定义
import uuid

from faker import Faker

table_structure = {
    'S_GUID': 'varchar(11)',
    'title': 'varchar(2000)',
    'content': 'longtext',
    'docreltime': 'datetime',
    # 'glcode': 'varchar(255)',
    # 'gltype': 'varchar(255)',
    'docpuburl': 'varchar(2000)',
    # 'sitename': 'varchar(255)',
    'jgfl': "varchar(5)",
    'validity': 'varchar(255)',
    'S_LAST_UPDATETIME': 'datetime',
    's_createtime': 'datetime'
}
fake = Faker(['zh_cn'])


# 生成随机字符串
def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


# 生成随机日期
def generate_random_date():
    year = random.randint(2023, 2024)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return f'{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}'


def generate_random_Chinese(length):
    return fake.text(random.randint(10, length))


# 生成插入语句
def generate_insert_statement(table_name, num_rows):
    insert_statements = []
    for _ in range(num_rows):
        values = []
        for column_name, column_type in table_structure.items():
            if column_name == 'S_GUID':
                value = uuid.uuid4()
            elif column_type == 'varchar(11)':
                value = generate_random_string(11)
            elif column_type == 'varchar(5)':
                value = table_name
            elif column_type == 'varchar(2000)':
                value = generate_random_Chinese(20)
            elif column_type == 'longtext':
                value = generate_random_Chinese(50)
            elif column_type == 'datetime':
                value = generate_random_date()
            elif column_type == 'varchar(255)':
                value = generate_random_string(25)
            else:
                value = ''
            values.append(f"'{value}'")
        insert_statement = f"INSERT INTO {table_name} ({', '.join(table_structure.keys())}) VALUES ({', '.join(values)});"
        insert_statements.append(insert_statement)

    return insert_statements


# 测试示例
table_name = 'zcwj'
num_rows = 10

if __name__ == '__main__':
    insert_statements = generate_insert_statement(table_name, num_rows)
    # 打印生成的插入语句
    for statement in insert_statements:
        print(statement)
