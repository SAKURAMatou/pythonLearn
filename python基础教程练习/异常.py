def func():
    try:
        return 1 / 0
        print('无异常')
    except Exception as e:
        print('异常发生行')
        raise e


#发生异常的地方不处理异常，由调用者处理异常
try:
    func()
except Exception as  e:
    print(e)
    print('调用的方法发生异常')
