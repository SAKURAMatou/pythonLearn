import time

# print(time.asctime())
t1 = (2021, 10, 30, 20, 47, 30, 6, 1, 0)
print(time.asctime(t1))
print(time.mktime(t1))
print(time.time())
print(time.localtime(time.time()))
print(time.strptime('2021-10-30', '%Y %m %d'))
