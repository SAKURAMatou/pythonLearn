import pandas as pd
import numpy as np

dataUrl = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
dataName = './chipotel_local.tsv'
chipo = pd.read_csv(dataName, sep='\t')
# chipo.to_csv(', encoding='utf-8', index=False, sep='\t')
# shape查看DataFrame的数据行，列的数量，返回一个tuple
# print(chipo.shape)
# print(chipo.info())
# # 列，行信息
# print(chipo.columns, '\n', chipo.index)
# 修改打印的设置
pd.set_option('display.max_column', None)
pd.set_option('display.width', 1000)
print(chipo.head())
print("*" * 10)
# 找订单最多的商品；商品名称分组，对订单那数量求和后排序
# c1 = chipo.groupby('item_name').sum('quantity').sort_values(by='quantity', ascending=False)
# print(c1.head(1)['quantity'])
# choice_description 中订单最多的商品
# ch2 = chipo.groupby("choice_description").sum('quantity').sort_values(by='quantity', ascending=False)
# print(ch2.head())
# 全部的订单数量
# print(chipo['quantity'].sum())
# print(chipo.quantity.sum())

# 把价格的数据类型转化为float;价格的值包含了$2.39，需要做字符串切片获取对应的价格忽略符号
# print(chipo.item_price.dtype)
# chipo.item_price.astype("float64")
chipo.item_price = chipo.item_price.apply(lambda x: float(x[1:]))
print(chipo.item_price.dtype)

# 数据中的所有数据收入是多少
chipo.item_price * chipo.quantity
