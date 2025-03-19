def create_file():
    try:
        with open("test.txt", "x", encoding="utf-8") as file:
            file.write("name: Mikhail Zakhodin \n")
            file.write("name: Ivan Ivanov \n")
            file.write("name: Angelina Borisova \n")
            file.write("name: Kolesnikov Artur \n")
            file.write("name: Gimli Gloin \n")
            file.write("name: Legolas Thranduil \n")
            file.write("name: Loren Thor \n")
    except FileExistsError:
        print("Файл уже существует!")


def read_file():
    try:
        with open("test.txt", "r", encoding="utf-8") as file:
            text = file.read()
            count_lines = len(text.splitlines())
            count_words = len(text.split())
            count_letters = 0
            for i in list(text):
                if i.isalpha():
                    count_letters += 1
            return count_lines, count_words, count_letters

    except FileExistsError:
        print("Файл не существует!")


def write_to_file(count_lines, count_words, count_letters):
    try:
        with open("test.txt", "a", encoding="utf-8") as file:
            file.write("\n Статистика файла: \n")
            file.write(f"Количество строк: {count_lines} \n")
            file.write(f"Количество слов: {count_words} \n")
            file.write(f"Количество букв: {count_letters} \n")
            print(f"Количество строк: {count_lines}")
            print(f"Количество слов: {count_words}")
            print(f"Количество букв: {count_letters}")
    except FileExistsError:
        print("Невозможно прочитать файл")


def main():
    create_file()
    count_lines, count_words, count_letters = read_file()
    write_to_file(count_lines, count_words, count_letters)


main()
