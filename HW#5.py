# Методы строк
web_site = 'www.my_site.com#about'
print(web_site.replace('#', '/'))
print(web_site[:] + 'ing')
print(" ".join('Ivanou Ivan'.split()[::-1]))
print("   sad    ".strip())
print("pARiS".capitalize())

# Методы спиков
print("Robin Singh".split())
print("I love arrays they are my favorite".split())
spisok = ['Ivan', 'Ivanou']
stroka = 'Minsk Belarus'
stroka = stroka.split()
print(f"Привет, {spisok[0]} {spisok[1]}! Добро пожаловать в "
      f"{stroka[0]} {stroka[1]}")
print(" ".join(["I", "love", "arrays", "they", "are", "my", "favorite"]))
spisok_2 = ['Privet', 22, 123, 123, 'sdfsdf', 445, 546456, 'Foo', 'Baz', 453]
spisok_2.insert(2, "center")
del spisok_2[6]
print(spisok_2)
