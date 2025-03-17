from datetime import datetime
try:
    first_date = str(input("Введите первую дату в формате 'ГГГГ-ММ-ДД': "))
    second_date = str(input("Введите вторую дату в формате 'ГГГГ-ММ-ДД': "))
    f = datetime.strptime(first_date, '%Y-%m-%d')
    s = datetime.strptime(second_date, '%Y-%m-%d')

    diff_days = abs(f - s).days
    print(f"Количество дней между первой датой {f.strftime('%Y-%m-%d')} и второй датой "
          f"{s.strftime('%Y-%m-%d')} равно: {diff_days}")
except ValueError:
    print("Одна из дат введена в неверном формате!")
