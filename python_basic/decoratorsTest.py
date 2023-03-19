def my_decorators(func):
    def wrapper(*args, **kwargs):
        print("befor function call")
        result = func(*args, **kwargs);
        print("after function call")
        return result

    return wrapper


@my_decorators
def add_function(x, y):
    return x + y


print(add_function(1, 3))
