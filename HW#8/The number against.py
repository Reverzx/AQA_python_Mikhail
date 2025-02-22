def solution(n, f_number):
    if n % 2 != 0:
        print('Длина окружности не четная')
        return False
    lenght = (n - 2) // 2
    i = 0
    while i != lenght + 1:
        f_number += 1
        if f_number == n:
            f_number = 0
        i += 1
    return f_number


assert solution(10, 1) == 6
assert solution(10, 2) == 7
assert solution(10, 3) == 8
assert solution(10, 4) == 9
assert solution(10, 5) == 0
assert solution(10, 6) == 1
assert solution(10, 7) == 2
assert solution(10, 8) == 3
