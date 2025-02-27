def cache(func):
    d = {}

    def wrapper(digit):
        if digit in d:
            print("Берем значение из кэша")
            return d.get(digit)
        else:
            result = func(digit)
            d[digit] = result

        return result

    return wrapper


@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))  # Вывод: 5
print(fibonacci(10))  # Вывод: 55
print(fibonacci(5))  # Вывод: 5 (значение взято из кэша)
