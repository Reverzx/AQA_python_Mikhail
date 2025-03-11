from HW13.Currency_converter import CurrencyConverter


class Bank:
    interest_rate = 0.1

    def __init__(self):
        self.start_balance = None
        self.name = None
        self.years = None
        self.client_id = '0000001'
        self.data_clients = {}
        self.converter = CurrencyConverter()

    def register_client(self, name):
        self.name = name
        self.data_clients[self.client_id] = {
            "name": name,
            "start_balance": None,
            "years": None
        }
        self.client_id = f"{(int(self.client_id) + 1):07d}"

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id in self.data_clients:
            self.client_id = client_id
            self.start_balance = start_balance
            self.years = years
            self.data_clients[client_id]["start_balance"] = self.start_balance
            self.data_clients[client_id]["years"] = self.years
            return (f"Открыт депозит клиента {self.data_clients[client_id]['name']} "
                    f"с номером {client_id}. Стартовый баланс {start_balance}. "
                    f"Срок депозита - {years} год(а)")
        else:
            return "Такого клиента не существует!"

    def calc_deposit_interest_rate(self, client_id):
        deposit_itog = round(self.data_clients[client_id]["start_balance"] *
                             (1 + self.interest_rate / 12)
                             ** (12 * self.data_clients[client_id]["years"]), 2)
        return deposit_itog

    # Добавил метод по конвертации валюты
    def converter_deposit(self, client_id, out_currency):
        if client_id not in self.data_clients:
            return "Клиент отсутсвует в базе"

        deposit_itog = self.calc_deposit_interest_rate(client_id)
        converted_value, currency = self.converter.exchange_currency("BYN",
                                                                     deposit_itog, out_currency)

        print(f"Депозит клиента {self.data_clients[client_id]['name']} "
              f"в валюте {currency}: {converted_value}")
        return converted_value, currency

    def close_deposit(self, client_id):
        if self.data_clients[client_id]["start_balance"]:
            self.data_clients[client_id]["start_balance"] = None
            self.data_clients[client_id]["years"] = None
        else:
            return "Клиент сначала должен открыть депозит"


bank = Bank()
bank.register_client(name="Pavel")
bank.register_client(name="Misha")
bank.open_deposit_account('0000001', start_balance=1000, years=1)
bank.open_deposit_account('0000002', start_balance=2000, years=2)

bank.calc_deposit_interest_rate('0000001')
bank.calc_deposit_interest_rate('0000002')
bank.converter_deposit('0000001', 'USD')

bank.close_deposit('0000002')
assert bank.calc_deposit_interest_rate('0000001') == 1104.71

bank_2 = Bank()
# bank_2 будет работать независимо от первого банка,
# клиенты у этого банка будут свои
bank_2.register_client(name="Gosha")
bank_2.register_client(name="Vitaliy")
bank_2.open_deposit_account('0000001', start_balance=5009, years=8)
bank_2.open_deposit_account('0000002', start_balance=20000, years=2)

bank_2.calc_deposit_interest_rate('0000001')
bank_2.calc_deposit_interest_rate('0000002')
