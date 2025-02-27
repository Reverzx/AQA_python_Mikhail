def validate_arguments(func):
    def wrapper(*args, **kwargs):
        for i in args:
            if not isinstance(i, (int, float)) or i <= 0:
                raise Exception("Аргумент функции не является положительным "
                                "или не является числом")
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)) or value <= 0:
                raise Exception("Аргумент функции не является положительным "
                                "или не является числом")
        return func(*args, **kwargs)
    return wrapper


@validate_arguments
def funct_digital(*args, **kwargs):
    return args


assert funct_digital(1, 2, 3, 6, dog=1)
