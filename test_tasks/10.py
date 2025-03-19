def decorator(*args, **kwargs):
    def wrapper(func):
        def inner(*f_args, **f_kwargs):
            print(args, kwargs)
            return func(*f_args, **f_kwargs)

        return inner

    return wrapper


@decorator(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one=1, two=2, three=3)
def identity(x):
    return x


print(identity(42))


@decorator()
def identity_2(x):
    return x


print(identity_2(42))
