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


if __name__ == "__main__":
    unittest.main()
