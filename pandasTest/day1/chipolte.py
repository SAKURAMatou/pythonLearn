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
# print(chipo.head())
# print("*" * 10)
# 找订单最多的商品；商品名称分组，对订单那数量求和后排序
# c1 = chipo.groupby('item_name').sum('quantity').sort_values(by='quantity', ascending=False);
# print(c1.head(1))
# 把价格的数据类型转化为float;价格的值包含了$2.39，需要做字符串切片获取对应的价格忽略符号
# print(chipo.item_price.dtype)
# chipo.item_price.astype("float64")#无法把含有特殊字符的字符串转float
# chipo.item_price = chipo.item_price.apply(lambda x: float(x[1:]))
# print(chipo.item_price.dtype)
# 数据集中的这段时间内的收入是多少：价格*数量然后求和
# 价格需要删除字符保留数组部分
# chipo.item_price = chipo.item_price.apply(lambda x: float(x.replace("$", '')))
# revenue = (chipo.quantity * chipo.item_price).sum()
# print(revenue)
# 数据中，共有多少订单
# print(chipo.order_id.value_counts().count())
# 每个订单的平均收入
chipo.item_price = chipo.item_price.apply(lambda x: float(x.replace("$", '')))
# 获得每个商品的收入作为一个新的列revenue
chipo1 = chipo.assign(revenue=lambda x: x.quantity * x.item_price)
# print(chipo1)
print(chipo1.groupby("order_id").sum().mean()['revenue'])
# print(chipo1.shape)
# print(chipo1.revenue.sum()/chipo1.shape[0])
#数据集中有多少不同的商品
print(chipo.item_name.value_counts().count())