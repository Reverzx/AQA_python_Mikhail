# Которая запрашивает у пользователя число и выводит его квадрат
def square(x: int) -> int:
    return x ** 2


print(square(int(input("Введи число, я тебе верну квадрат: "))))


# Которая запрашивает у пользователя число и определяет, является ли
# оно четным или нечетным
def even(y: int) -> int:
    return True if y % 2 == 0 else False


print(even(int(input("Введи число, я True если чет: "))))
