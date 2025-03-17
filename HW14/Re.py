import re


def data_file():
    try:
        with open("Text_with_data.txt", "r", encoding="utf-8") as file:
            file_str = file.read()
            pattern = r"\b\d{2}\.\d{2}\.\d{4}\b"
            return re.findall(pattern, file_str)

    except FileNotFoundError:
        print("Невозможно прочитать файл")


print(data_file())


def password_validate(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{4,}$"
    print(f"Пароль {password} валидный!") if re.match(pattern, password) \
        else print(f"Пароль {password} не соответствует требованиям!")
    pass


password_validate("Ha12d")
password_validate("ABC1")
password_validate("1234342")
password_validate("Hh1")
password_validate("")
password_validate("Hdsf13GDgdg")
password_validate("a12d321df")


def repair_words(text):
    pattern = r"\b(\w+)(\s+\1)+\b"
    fixed_text = re.sub(pattern, r"\1", text)
    return fixed_text


text = ("Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. "
        "Смешно, не не правда ли? Не нужно портить хор хоровод.")
correct_words = repair_words(text)
print(correct_words)
