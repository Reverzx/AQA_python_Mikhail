#    Из заданной строки получить нужную строку:

a = "String"
# s=""
for i in a:
    print(i*2, end="")
# print(s)
print()
# "Hello World" => "HHeelllloo  WWoorrlldd"
b = "Hello World"
for i in b:
    print(i*2, end="")
# "1234!_ " => "11223344!!__  "
print()
c = "1234!_ "
for i in c:
    print(i*2, end="")
print()

# Если х в квадрате больше 1000 - пишем "Hot" иначе - "Nope"

# '50' == "Hot"
# 4 == "Nope"
# "12" == "Nope"
# 60 == "Hot"
strin = ['50', 4, "12", 60]
for x in strin:
    if int(x)**2 > 1000:
        print("Hot")
    else:
        print("Nope")

# Сложите все числа в списке, они могут быть отрицательными, если список пустой вернуть 0

# [] == 0
# [1, 2, 3] == 6
# [1.1, 2.2, 3.3] == 6.6
# [4, 5, 6] == 15
# range(101) == 5050
ss = [50, 4, 12, 60]
if not ss:
    print(0)
else:
    print(sum(ss))


# Подсчет букв. Дано строка и буква => "fizbbbuz","b", нужно подсчитать сколько раз буква b встречается в заданной
# строке 3

#"Hello there", "e" == 3
#"Hello there", "t" == 1
#"Hello there", "h" == 2
#"Hello there", "L" == 2
#"Hello there", " " == 1

sz = "fizbbbuz"
bukv = "b"
print(sz.count(bukv))
print()
# Напишите программу, которая перебирает последовательность от 1 до 100. Для чисел кратных 3 она должна написать:
# "Fuzz" вместо печати числа, а для чисел кратных 5 печатать "Buzz". Для чисел которые кратны 3 и 5 надо печатать
# "FuzzBuzz". Иначе печатать число.

for i in range(1, 101):
    if i%3==0 and i%5==0:
        print("FuzzBuzz")
    elif i%3==0:
        print("Fuzz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

print()

# Напишите код, который возьмет список строк и пронумерует их. Нумерация начинается с 1, имеет : и пробел
# [] => []
# ["a", "b", "c"] => ["1: a", "2: b", "3: c"]

dd={}
ds=0
sss = ["a", "b", "c"]
for i in sss:
    ds+=1
    dd.update({ds:i})
print(dd)
print()
# Проверить, все ли элементы одинаковые

# [1, 1, 1] == True
# [1, 2, 1] == False
# ['a', 'a', 'a'] == True
# [] == True
ssss = ['a', 'a', 'a']
if ssss.count(ssss[0]) == len(ssss):
    print(True)
else:
    print(False)

if len(set(ssss)) == 1:
    print(True)
else:
    print(False)

# Создайте программу, которая, принимая массив имён, возвращает строку описывающая количество лайков (как в Facebook).

#likes() -> "no one likes this"
#likes("Ann") -> "Ann likes this"
#likes("Ann", "Alex") -> "Ann and Alex like this"
#likes("Ann", "Alex", "Mark") -> "Ann, Alex and Mark like this"
#likes("Ann", "Alex", "Mark", "Max") -> "Ann, Alex and 2 others like this"