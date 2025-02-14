x = list(map(int,input("Введите размеры неповторяющихся статуй через пробел: ").split()))
a = []
i = min(x)+1
while i < max(x):
    if i not in x:
        a.append(i)
    i += 1
print(f'Не хватает статуй под номерами: {a}, всего не хватает {len(a)} статуй')
