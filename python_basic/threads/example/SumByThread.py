import unittest
from multiprocessing import Queue, Process
from time import time


class SumByThreadTest(unittest.TestCase):
    def test_sum(self):
        """单线程计算求和"""
        total = 0
        number_list = [x for x in range(1, 100000001)]
        start = time()
        for number in number_list:
            total += number
        print(total)
        end = time()
        print('Execution time: %.3fs' % (end - start))

    def test_sum_threads(self):
        """通过多进程的方式分片计算求和，并计算总时间"""
        max = 100000000
        number_list = [x for x in range(1, max + 1)]
        result_queue = Queue()
        processes = []
        index = 0
        len = 8
        lenBy = int(max / len)
        print(lenBy, type(lenBy))
        for _ in range(len):
            p = Process(target=task_handler, args=(number_list[index:index + lenBy], result_queue))
            index += lenBy
            processes.append(p)
            p.start()
        start = time()
        # 等待所有进程执行完毕
        for p in processes:
            p.join()

        # 从每个进程的结果中获取分片的结果，并求和
        total = 0
        while not result_queue.empty():
            total += result_queue.get()
        print(total)
        end = time()
        print('Execution time: %.3fs' % (end - start))


def task_handler(number_list, queue):
    total = 0
    for i in number_list:
        total += i
    queue.put(total)
