# Быки и коровы
n = input('Загадайте 4-значное число: ')
bulls = 0
if len(n) != len(set(n)):
    print('Не правильное число. Введите число с неповторяющимися цифрами')
else:
    while bulls != 4:
        bulls = 0
        cows = 0
        a = input('Угадайте 4-значное число: ')
        for i in range(4):
            if n[i] == a[i]:
                bulls += 1
            if n[i] in a:
                cows += 1
        cows = cows - bulls
        if len(a) != len(set(a)):
            print('Не правильное число. Введите число с неповторяющимися цифрами')
        elif bulls == 4:
            print("Вы выиграли!")
            break
        else:
            print(f'{cows} коров, {bulls} быков')
