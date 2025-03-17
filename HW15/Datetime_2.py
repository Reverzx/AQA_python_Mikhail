from datetime import datetime

try:
    now = datetime.now().date()
    first_date = str(input("Введите дату в формате 'ГГГГ-ММ-ДД': "))
    f = datetime.strptime(first_date, '%Y-%m-%d').date()
    diff_days = (f - now).days
    if diff_days > 0:
        print(f"Вы ввели будущую дату. Она наступит через {abs(diff_days)} дней")
    elif diff_days < 0:
        print(f"Вы ввели прошедшую дату. Она была {abs(diff_days)} дней назад")
    else:
        print("Вы ввели текущую дату")

except ValueError:
    print("Дата введена в неверном формате!")
