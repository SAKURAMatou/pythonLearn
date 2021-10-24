# def check_index(key):
#     """指定的键是否是可接受的索引？键必须是非负整数，才是可接受的。如果不是整数，
#     将引发TypeError异常；如果是负数，将引发Index
#     Error异常（因为这个序列的长度是无穷的）"""
#     if not isinstance(key, int): raise TypeError
#     if key < 0: raise IndexError
#
#
# class ArithmeticSequence:
#     def __init__(self, start=0, step=1):
#         """初始化序列
#         changed：一个字典，包含用户修改的信息"""
#         self.start = start
#         self.step = step
#         self.changed = {}
#
#     def __getitem__(self, key):
#         """从序列中获取元素"""
#         check_index(key)
#         try:
#             return self.changed[key]
#         except:
#             return self.start + key * self.step
#
#     def __setitem__(self, key, value):
#         """修改值"""
#         check_index(key)
#         self.changed[key] = value
#
# s=ArithmeticSequence(1,2)
# print(s[4])
# s[4]=2
# print(s[4])
# print(s[5])

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    size = property(get_size, set_size)


r = Rectangle()
# r.set_size((12, 4))
print(r.size((12, 4)))
