from time import time as time_ns


def create_list_range(a, b):
    return [_ for _ in range(a, b)]


def get_stars(a):
    return "*" * a


def timer(f):
    def func(*args, **kwargs):
        before = time_ns()
        rv = f(*args, **kwargs)
        print(time_ns() - before)
        return rv

    return func
