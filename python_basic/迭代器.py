# 迭代器
# class Fibs(object):
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         return self.a
#
#     def __iter__(self):
#         return self
#
#
# f = Fibs()
# for i in f:
#     if i > 100:
#         print(i)
#         break
# 生成器\
# 讲列表展开的函数
nested = [[1, 2], [1, 2, 3, 4], [5, 6, 7, 8, 9]]


# def flatten(nested):
#     for i in nested:
#         for j in i:
#             yield j
#
#

def flatten(nested):
    try:
        try:
            nested + ""
        except TypeError:
            pass
        else:
            TypeError
        for sub_List in nested:
            for e in flatten(sub_List):
                yield e
    except TypeError:
        yield nested


for i in flatten(nested):
    print(i, end="-")
