# Быки и коровы
n = input('Загадайте 4-значное число: ')
b = 0
if len(n) != len(set(n)):
    print('Не правильное число')
else:
    while b != 4:
        b = 0
        c = 0
        a = input('Угадайте 4-значное число: ')
        for i in range(4):
            if n[i] == a[i]:
                b += 1
            if n[i] in a:
                c += 1
        c = c - b
        if len(a) != len(set(a)):
            print('Не правильное число')
        elif b == 4:
            print("Вы выиграли!")
            break
        else:
            print(f'{c} коров, {b} быков')
