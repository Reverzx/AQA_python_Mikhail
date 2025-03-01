def validate_number(func):
    def wrapper(*args):
        result = func(*args)
        if not isinstance(result, (int, float)):
            print("Результат функции не является числом")
            return False

        return result
    return wrapper


@validate_number
def funct_number(*args):
    return sum(args)


@validate_number
def funct_str(x):
    return x


assert funct_number(1, 2, 3, 6)
assert not funct_str('Hello')
