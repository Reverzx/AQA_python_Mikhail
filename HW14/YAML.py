import yaml
import re

data = {
    "books": [
        {"title": "1984", "author": "George Orwell", "year": 1949},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
        {"title": "Moby-Dick", "author": "Herman Melville", "year": 1851}
    ]
}

with open("books.yaml", "w", encoding="utf-8") as file:
    yaml.dump(data, file, allow_unicode=True)

with open("books.yaml", "r", encoding="utf-8") as file:
    file_str = file.read()
    title_pattern = r'title:\s*(.+)'
    author_pattern = r'author:\s*(.+)'
    year_pattern = r'year:\s*(\d+)'
    name_list = re.findall(title_pattern, file_str)
    author_list = re.findall(author_pattern, file_str)
    year_list = re.findall(year_pattern, file_str)
    for n, a, y in zip(name_list, author_list, year_list):
        print(f"Название книги: {n}; Автор: {a}; Год издания: {y}")

with open("books.yaml", "w", encoding="utf-8") as file:
    title = input("Введите название книги: ")
    author = input("Введите имя и фамилию автора через пробел: ")
    while True:
        try:
            year = int(input("Введите год выпуска книги (только цифры): "))
            break
        except ValueError:
            print("Пожалуйста, введите корректный год (число).")
    data['books'].append({
        'title': title,
        'author': author,
        'year': year
    })
    print("Книга успешно добавлена!")
    # {"title": title, "author": author, "year": year}
    # f'"title": {title}, "author": {author}, "year": {year}'
    yaml.dump(data, file, allow_unicode=True)
