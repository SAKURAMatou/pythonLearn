# from turtle import *
#
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
# print(repr("123\n456"))
# print(r'789\n456')
# print('cat:\N{cat}')

# url = input('输入地址：')
# print(url[10:1])
# 列表的切片
# my_list = ['P']
# my_list[1:] = list('ython')
# print(my_list)

# import  copy
# print(copy.__file__)


def conflict(state, nextX):
    """检测位置是否冲突"""
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
        else:
            return False


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


import random

# print(prettyprint(random.choice(list(queens(4)))))
import  sys
print(sys.argv)