from threading import Thread, Lock
from time import sleep


class AccountWithOutLock:
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


class AddmoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main_no_lock():
    account = AccountWithOutLock()
    thresds = []
    for i in range(0, 10):
        t = AddmoneyThread(account, 1)
        thresds.append(t)
        t.start()
    # 等所有线程执行完成
    for i in thresds:
        i.join()
    print('账户余额为：%d' % account.balance)


class AccountWithLock:
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 现货区锁在执行后续余额变更
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.1)
            self._balance = new_balance
        finally:
            # finally中执行锁的释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


def main_lock():
    account = AccountWithLock()
    thresds = []
    for i in range(0, 10):
        t = AddmoneyThread(account, 1)
        thresds.append(t)
        t.start()
    # 等所有线程执行完成
    for i in thresds:
        i.join()
    print('账户余额为：%d' % account.balance)


if __name__ == '__main__':
    main_lock()
