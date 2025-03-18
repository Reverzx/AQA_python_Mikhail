from datetime import datetime


def days_diff(first_date, second_date):
    try:
        f = datetime.strptime(str(first_date), '%Y-%m-%d')
        s = datetime.strptime(str(second_date), '%Y-%m-%d')
        diff_days = abs(f - s).days
        print(f"Количество дней между первой датой {f.date()} и второй датой "
              f"{s.date()} равно: {diff_days}")
        return diff_days
    except ValueError:
        print("Одна из дат введена в неверном формате!")
        return None


print(days_diff(input("Введите первую дату в формате 'ГГГГ-ММ-ДД': "),
                input("Введите вторую дату в формате 'ГГГГ-ММ-ДД': ")))
