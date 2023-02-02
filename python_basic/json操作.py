import json

data = [{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}]
# print(type(data))
# print(json.dumps(data))
# # 格式化参数输出
# print(json.dumps(data, sort_keys=True))
# print(json.dumps(data, indent=4))
str='{"a":1,"b":2,"c":3,"d":4,"e":5}'
print(json.loads(str))
