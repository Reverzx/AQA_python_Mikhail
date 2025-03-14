import yaml

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
    books_yaml = yaml.safe_load(file)
    for i in books_yaml['books']:
        print(f"Название книги: {i['title']}; Автор: {i['author']}; Год издания: {i['year']}")

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
    yaml.dump(data, file, allow_unicode=True)
