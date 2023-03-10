import unittest
import numpy as np
import pandas as pd
import re


class dlTestCase(unittest.TestCase):
    def setUp(self):
        self.testData = {"A": [10, 20, 30, 40, 20],
                         "B": [11, 22, 33, 44, 11],
                         "C": [44, 55, 66, 77, 88]}
        self.sdf = pd.DataFrame(self.testData)
        print(self.sdf, '\n', '*' * 15)
        """setUp,tearDown，可以设置测试开始前与完成后需要执行的指令"""
        pass

    def tearDown(self):
        """setUp,tearDown，可以设置测试开始前与完成后需要执行的指令"""
        pass

    def test_dl1(self):
        data = np.random.randint(100, 120, size=50)
        print(data)
        print(pd.Series(data).value_counts())

    def test_dl2(self):
        print(self.sdf.groupby("A").sum())
        print(self.sdf.groupby("A").sum().mean())

    def test_jsonReTest(self):
        str = '<script>__INITIAL_STATE__={"esa":[{"dsa":"DAS"}]}</script>'
        g = re.search(r'(?<=__INITIAL_STATE__=).*(?=</script>)', str)
        print(g, g.group(0))
        numbers = [1, 2, 3, 4, 5]
        print([num * num for num in numbers])

    def test_unique(self):
        df = pd.DataFrame({"A": [10, 20, 30, 40, 20, 50, 10, 40],
                           "B": [10, 22, 30, 44, 20, 30, 50, 44],
                           "C": [10, 55, 66, 77, 88, 50, 60, 75]})
        print(df)
        print(df.drop_duplicates())
        print(df.drop_duplicates(['B', 'C']))

    def test_column(self):
        df = self.sdf
        # print(df['A'])
        print("#" * 15)
        print(df[['A', 'C']])


if __name__ == "__main__":
    unittest.main()
