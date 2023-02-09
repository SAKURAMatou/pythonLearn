import unittest
import numpy as np
import pandas as pd

"""pandas练习第二课"""


class FilterSortTest(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('././chipotle_local.tsv')
        pd.set_option('display.max_column', None)
        pd.set_option('display.width', 1000)
        print(self.df.head(20))
        pass

    def test_get_data_local(self):
        url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
        df = pd.read_csv(url, sep='\t')
        df.to_csv('./chipotle_local.tsv')

    def test_one(self):
        """
        How many products cost more than $10.00;有多少商品的价格超过10？
        先转化价格一列数据为数字类型，
        找到价格超过10的数据，
        """
        print("test_one")
        chipo = self.df
        # assign方法对列数据进行操作时需要使用列表推导式作为入参函数
        # chipo.item_price返回一个series对象，循环时获取到一个迭代器，列表推导式驱动时可以对其中每个数据进行操作
        # chipo.assign(price=lambda x: print(x.item_price))
        chipo = chipo.assign(price=lambda x: [float(value[1:]) for value in chipo.item_price])
        # print(str(i) for i in c.item_price[:])
        # chipo.item_price = chipo.item_price.apply(lambda x: float(x[1:]))
        # 转化dataframe中列的数据两种方法1、使用assign+列表推导式
        # 2、使用apply操作列得到新的数据并给列赋值，但不能新增列
        print(chipo.query('price>10').item_name.count())
        # print(chipo[chipo.price == 3.39].item_name.nunique())

    def test_two(self):
        """ What is the price of each item?打印商品名称和商品价格"""
        chipo = self.df
        # item_price是商品数量*商品单价后的结果，获取价格的话需要转化计算得到商品单价
        # 按照数量，商品名称去重之后得到数量名称相同的数据，再找到其中数量是1的即为商品和单价
        # 1、去重
        chipo_unique = chipo.drop_duplicates(subset=['item_name', 'quantity'])
        # 2、找到数量为1的数据
        # res = chipo_unique.query("quantity==1")[['item_name', 'item_price']]
        # print(res)
        chipo_one_prod = chipo_unique[chipo_unique['quantity'] == 1]
        print(chipo_one_prod[['item_name', 'item_price']])

    def test_thress(self):
        """
        What was the quantity of the most expensive item ordered;
        最贵的订单的商品数量;排序时需要根据价格的数字排序而不是字符串
        """
        chipo = self.df
        chipo = chipo.assign(price=lambda x: [float(value[1:]) for value in chipo.item_price])
        # print(chipo.iloc[3598])
        chipo_sorted = chipo.sort_values("price", ascending=False)
        print(chipo_sorted.head())
