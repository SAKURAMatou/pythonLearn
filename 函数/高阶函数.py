def func(g, arr):
    return [g(x) for x in arr]


def double(x):
    return 2 * x


print(func(double, [1, 2, 3]))
