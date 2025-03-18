from datetime import datetime


def days_diff_now(date):
    try:
        now = datetime.now().date()
        f = datetime.strptime(str(date), '%Y-%m-%d').date()
        diff_days = (f - now).days
        if diff_days > 0:
            print(f"Вы ввели будущую дату. Она наступит через {abs(diff_days)} дней")
        elif diff_days < 0:
            print(f"Вы ввели прошедшую дату. Она была {abs(diff_days)} дней назад")
        else:
            print("Вы ввели текущую дату")
        return abs(diff_days)
    except ValueError:
        print("Дата введена в неверном формате!")
        return None


print(days_diff_now(input("Введите дату в формате 'ГГГГ-ММ-ДД': ")))
