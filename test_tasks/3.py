# Суммирование. Необходимо подсчитать сумму всех чисел до заданного:
def summa(n: int) -> int:
    return n * (n + 1) // 2


assert summa(1) == 1
assert summa(2) == 3
assert summa(8) == 36
assert summa(22) == 253
assert summa(100) == 5050
print(summa(100))
