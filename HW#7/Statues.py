# x = [6, 1, 3, 8, 15]
x = list(map(int,input("Введите размеры статуй через пробел: ").split()))
minim = min(x)
maks = max(x)
print(f"Не хватает {maks - minim - len(set(x)) +1} статуи")
