def typed(type):
    def decorator(func):
        def wrapper(*args):
            converted_args = [type(arg) for arg in args]
            result = func(*converted_args)
            return result

        return wrapper

    return decorator


@typed(type=str)
def add(a, b):
    return a + b


assert add("3", 5) == "35"
assert add(5, 5) == "55"
assert add('a', 'b') == "ab"


@typed(type=int)
def add(a, b, c):
    return a + b + c


assert add(5, 6, 7) == 18


@typed(type=float)
def add(a, b, c):
    return a + b + c


assert add(0.1, 0.2, 0.4) == 0.7000000000000001
