from contextlib import contextmanager


@contextmanager
def my_context():
    # def __enter__():
    #     print("entering context")
    print("entering context")
    # yield关键字之前的代码在进入上下文管理器之前执行，yield关键字之后的代码在进入上下文管理器之后执行
    yield
    print('具体业务内容')
    print('exiting context')
    # def __exit__():
    #     print('exiting context')


if __name__ == '__main__':
    with my_context():
        print('inside context')
