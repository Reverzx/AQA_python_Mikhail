class CurrencyConverter:
    dict_converter = {
        "USD": 3.24,  # 1 USD = 3.24 BYN
        "EUR": 3.40,  # 1 EUR = 3.41 BYN
        "BYN": 1.0  # 1 BYN = 1 BYN
    }

    def __init__(self):
        self.out_currency = None
        self.amount = None
        self.in_currency = None

    def exchange_currency(self, in_currency, amount, out_currency="BYN"):
        self.in_currency = in_currency
        self.amount = amount
        self.out_currency = out_currency
        new_value = ((self.dict_converter[in_currency] * self.amount) /
                     self.dict_converter[out_currency])
        return round(new_value, 2), out_currency


class Person:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


converter = CurrencyConverter()

vasya = Person('USD', 10)
petya = Person('EUR', 5)

# Если валюта не задана, то конвертация происходит в BYN:
print(converter.exchange_currency(vasya.currency, vasya.amount))
print(converter.exchange_currency(petya.currency, petya.amount, 'USD'))

assert converter.exchange_currency(vasya.currency, vasya.amount) == (32.4, "BYN")
assert converter.exchange_currency(petya.currency, petya.amount) == (17.0, "BYN")

# Конвертация в заданную валюту BYN:
assert converter.exchange_currency(vasya.currency, vasya.amount, 'EUR') == (9.53, "EUR")
assert converter.exchange_currency(petya.currency, petya.amount, 'USD') == (5.25, "USD")
