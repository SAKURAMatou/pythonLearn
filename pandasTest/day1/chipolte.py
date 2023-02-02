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
# 找订单最多的商品；商品名称分组，对订单那数量求和后排序
c1 = chipo.groupby('item_name').sum('quantity').sort_values(by='quantity', ascending=False);
print(c1.head(1))
