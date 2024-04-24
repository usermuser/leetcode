# d = {"a": 1, "b": 2}
# d.pop("a")
# d.pop("z", None)
# print(d)

from functools import wraps

def mydeco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"{func(*args, **kwargs)}!!!"

    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper

@mydeco
def myadd(a, b):
    """myadd docstring"""
    return a + b

@mydeco
def mysum(*args):
    """mysum docstring"""
    total = 0
    for one_item in args:
        total += one_item
    return total


if __name__ == '__main__':
    print(myadd(10,20))
    print(mysum(10, 20, 30, 40, 50))

    print(myadd.__name__)
    print(mysum.__name__)

    # help(myadd)
    # help(mysum)

    print(myadd.__doc__)
    print(mysum.__doc__)