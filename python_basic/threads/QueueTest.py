import queue
import time
from threading import Thread, Lock

exitFlag = 0


def process_data(threadName, queue):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = queue.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)


class MyThread(Thread):
    def __init__(self, threadID, name, queue):
        Thread.__init__(self)
        self._threadID = threadID
        self._name = name
        self._queue = queue

    def run(self):
        print("开启线程：" + self._name)
        process_data(self._name, self._queue)
        print("退出线程：" + self._name)


queueLock = Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]

for tName in threadList:
    thread = MyThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

exitFlag = 1

# 等待所有线程执行完成
for t in threads:
    t.join()
print("退出主线程")
