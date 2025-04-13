from Currency_converter import CurrencyConverter


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
        current_id = self.client_id
        self.data_clients[self.client_id] = {
            "name": name,
            "start_balance": None,
            "years": None
        }
        self.client_id = f"{(int(self.client_id) + 1):07d}"
        return current_id

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id in self.data_clients:
            self.client_id = client_id
            self.start_balance = float(start_balance)
            self.years = int(years)
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
client_id = None


def register_test_client():
    global client_id
    client_id = bank.register_client("Test")
    return client_id


def get_client_data():
    return bank.data_clients[client_id]


def open_deposit(balance, years):
    return bank.open_deposit_account(client_id, balance, years)


def open_deposit_for_invalid_client():
    return bank.open_deposit_account("9000000", 1000, 1)


def calculate_interest():
    return bank.calc_deposit_interest_rate(client_id)


def convert_to_currency(currency):
    return bank.converter_deposit(client_id, currency)


def close_deposit():
    return bank.close_deposit(client_id)
