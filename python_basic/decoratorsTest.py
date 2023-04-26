import time
from multiprocessing import RLock, Lock


def my_decorators(func):
    def wrapper(*args, **kwargs):
        print("befor function call")
        result = func(*args, **kwargs);
        print("after function call")
        return result

    return wrapper


def record_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} cost {end_time - start_time} seconds')
        return result

    return wrapper


@record_time
def add_function(x, y):
    time.sleep(5)
    return x + y


# print(add_function(1, 3))
# 通过装饰器实现单例模式
def singleton(cls):
    instances = {}
    locker = Lock()

    def wrap(*args, **kwargs):
        """加锁前后对单例对象是否存在进行判断，类比java中的单例模式"""
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrap


@singleton
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person('Tome', 12)
person2 = Person("Tony", 18)
print(person1 == person2)
