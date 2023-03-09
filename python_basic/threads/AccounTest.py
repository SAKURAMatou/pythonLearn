from time import sleep


class AccountWithOutLock():
    """账号类，没有对账号内的余额加锁，线程不安全"""

    def __init__(self):
        self._balance = 0

    def deposit(self, money):
        # 计算存款后的余额
        new_balance = self._balance + money
        # 线程暂停0.1s模拟实际场景
        sleep(0.1)
        # 修改账户余额
        self._balance = new_balance

    @property
    def balance(self):
        return self._balance
