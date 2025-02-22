def solution(number):
    if not number:
        print("Номер карты не должен быть пустой!")
        return False
    if not str(number).isdigit():
        print("Номер карты должен содержать только только цифры!")
        return False

    value = (str(number))[::-1]
    new_value = 0
    for index, char in enumerate(value):
        if index % 2 != 0:
            char = int(char) * 2
            if char > 9:
                char = int(str(char)[0]) + int(str(char)[1])
            new_value += char
        else:
            new_value += int(char)
    if new_value % 10 == 0:
        return True
    else:
        return False


assert not solution(4561261212345464)
assert solution(4561261212345467)
assert solution(378282246310005)
