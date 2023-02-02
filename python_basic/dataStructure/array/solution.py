# 返回字符串最后一个单词的长度
# def countLastWords(str):
#     arr = str.split(" ")
#     a = len(arr)
#     return len(arr[a - 1])
#
#
# str = input("")
#
# print(countLastWords(str))

# 计算某字符出现次数
# def countStr(str, waitCount):
#     str = str.lower()
#     waitCount = waitCount.lower()
#     return str.count(waitCount)
#
#
# str = input()
# waitCount = input()
# print(countStr(str, waitCount))

# 随机数
# while True:
#     n = int(input())
#     my_arr = {}
#     while n > 0:
#         key = int(input())
#         my_arr[key] = key
#         n = n - 1
#     # 去重
#
#     # 排序
#     sorted(my_arr, key)
#     for i in my_arr:
#         print(i)


my_arr = {'1': 3, '2': 2}
# print(sorted(my_arr.items(), key=lambda x: x[1]))
print(my_arr.items())
