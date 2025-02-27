def typed(type):
    def decorator(func):
        def wrapper(*args):
            converted_args = [type(arg) for arg in args]
            result = func(*converted_args)
            return result

        return wrapper

    return decorator


@typed(type=str)
def add_one(a, b):
    return a + b


assert add_one("3", 5) == "35"
assert add_one(5, 5) == "55"
assert add_one('a', 'b') == "ab"


@typed(type=int)
def add_two(a, b, c):
    return a + b + c


assert add_two(5, 6, 7) == 18


@typed(type=float)
def add_three(a, b, c):
    return a + b + c


assert add_three(0.1, 0.2, 0.4) == 0.7000000000000001
