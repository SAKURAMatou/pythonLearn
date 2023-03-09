import unittest
import random
from multiprocessing import Process
from os import getpid
from threading import Thread
from time import sleep, time
from typing import Optional, Callable, Any, Iterable, Mapping


class SimplePythonThread(unittest.TestCase):

    def test_no_thread(self):
        start = time()
        download_task('Python从入门到住院.pdf')
        download_task('Peking Hot.avi')
        end = time()
        print('总共耗费了%.2f秒.' % (end - start))

    def test_with_process(self):
        start = time()
        # Process创建进程对象；创建不同的进程之后，执行具体方法时可以看到进程的pid不一致
        p1 = Process(target=download_task_with_thread, args=('Python从入门到住院.pdf',))
        p2 = Process(target=download_task_with_thread, args=('Peking Hot.avi',))
        p1.start()
        p2.start()
        p1.join()  # 表示等待进程执行结束
        p2.join()
        end = time()
        print('总共耗费了%.2f秒.' % (end - start))

    def test_with_thread(self):
        start = time()
        # Thread创建线程对象；在同一个进程中用不同的线程执行，和Process区别在于，pid相同表示是在同一个进程内执行
        p1 = Thread(target=download_task_with_thread, args=('Python从入门到住院.pdf',))
        p2 = Thread(target=download_task_with_thread, args=('Peking Hot.avi',))
        p1.start()
        p2.start()
        p1.join()  # 表示等待线程执行结束
        p2.join()
        end = time()
        print('总共耗费了%.2f秒.' % (end - start))

    def test_self_thread(self):
        start = time()
        t1 = DownloadTask('Python从入门到住院.pdf')
        t2 = DownloadTask('Peking Hot.avi')
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        end = time()
        print('总共耗费了%.2f秒.' % (end - start))


# 继承Thread创建自定义的多线程
class DownloadTask(Thread):

    def __init__(self, filename) -> None:
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = random.randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def download_task(filename):
    """单线程下载模拟方法"""
    print('开始下载%s...' % filename)
    time_to_download = random.randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def download_task_with_thread(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = random.randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
