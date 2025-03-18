def palindrom(s) -> bool:
    return True if s == s[::-1] else False


assert palindrom('анна')
assert palindrom('потоп')
assert palindrom('1221')
assert not palindrom('1234')

print(palindrom(input('Введи слово или число: ')))
