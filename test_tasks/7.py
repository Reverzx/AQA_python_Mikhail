def f(s, n):
    try:
        left = s[:n]
        right = left[-2::-1]
        return left + right
    except ValueError:
        print("n не может быть больше длины строки s")


s = "abcdefghijklmnopqrstuvwxyz"
print(f(s, 1))
print(f(s, 2))
print(f(s, 3))
print(f(s, 4))
