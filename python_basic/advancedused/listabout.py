import itertools
import unittest
import random


class ListAboutTest(unittest.TestCase):
    def test_list_generate(self):
        prices = {
            'AAPL': 191.88,
            'GOOG': 1186.96,
            'IBM': 149.24,
            'ORCL': 48.44,
            'ACN': 166.89,
            'FB': 208.09,
            'SYMC': 21.29
        }
        # 用股票价格大于100元的股票构造一个新的字典
        prices2 = {key: value for key, value in prices.items() if value > 100}
        print(prices2)

    def test_list_genere(self):
        names = ['关羽', '张飞', '赵云', '马超', '黄忠']
        courses = ['语文', '数学', '英语']
        scores = [[None] * len(courses) for _ in range(len(names))]
        for row, name in enumerate(names):
            for col, course in enumerate(courses):
                scores[row][col] = random.randint(60, 100)
                print(scores)

    def test_itertools(self):
        # 产生ABCD的全排列
        premutations = itertools.permutations("ABCD")
        print(len(list(premutations)))
        # 生成 "ABCD"的4选2结果
        combinations = itertools.combinations("ABCD", 2)
        print(list(combinations))

        # 产生ABCD和123的笛卡尔积
        product = itertools.product("ABCD", "123")
        print(list(product))
        # 产生ABCD的无限循环序列；不会自己结束，需要手动结束

        count = 0
        for c in itertools.cycle('ABCD'):
            if count > 5:
                break
            else:
                print(c)
                count += 1
        # count(初始值=0, 步长值=1):count 迭代器会返回从传入的起始参数开始的均匀间隔的数值
        for i in itertools.count(5, 3):
            if i > 20:
                break
            else:
                print(i)

        # 迭代器合并：extend合并列表方法 my_list.extend(numbers)；只能合并两个，chain能合并多个
        chain = itertools.chain(['A', 'B'], list(range(4)))
        print(list(chain))
