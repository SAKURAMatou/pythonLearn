import itertools
import unittest
import random
import collections


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

    def test_collections(self):
        # collections.namedtuple；返回一个指定成员的子类
        Person = collections.namedtuple('Person', ['name', 'age'])
        person = Person(name='张三', age=18)
        print(person.name, person.age, person[0], person[1])
        # deque 双端队列，是列表的替代实现。Python中的列表底层是基于数组来实现的，而deque底层是双向链表，因此当你需要在头尾添加和删除元素时，deque会表现出更好的性能，渐近时间复杂度为$O(1)$。
        queue = collections.deque([1, 2, 3])
        queue.append(4)  # 在队列右边添加数据
        print(queue)
        queue.appendleft(5)  # 队列左边添加数据
        print(queue)

        words = [
            'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
            'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
            'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
            'look', 'into', 'my', 'eyes', "you're", 'under'
        ]
        # Counter：dict的子类，键是元素，值是元素的计数，它的most_common()方法可以帮助我们获取出现频率最高的元素
        counter = collections.Counter(words)
        print(counter)
        print(counter.most_common(3))

        # OrderedDict：dict的子类，它记录了键值对插入的顺序，看起来既有字典的行为，也有链表的行为(有序的字典)
        l = [('a', 1), ('c', 3), ('b', 2)]
        ordered_dict = collections.OrderedDict(l)
        print(list(ordered_dict.keys()))
        # defaultdict：类似于字典类型，但是可以通过默认的工厂函数来获得键对应的默认值，相比字典中的setdefault()方法，这种做法更加高效。
        # 创建一个没有key但又默认值的类似字典的对象
        default_dict = collections.defaultdict(int)
        print(default_dict['a'])

        #
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'e': 3, 'd': 4}
        chain_map = collections.ChainMap(dict1, dict2)
        for key, value in chain_map.items():
            print(key, value)

    def test_advanced_func(self):
        items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
        print(items1)
