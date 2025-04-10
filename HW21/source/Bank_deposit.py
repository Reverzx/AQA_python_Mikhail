from HW13.Currency_converter import CurrencyConverter
from loguru import logger


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
        logger.debug(f"Клиент {self.name} успешно зарегистрирован")

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id in self.data_clients:
            self.client_id = client_id
            self.start_balance = start_balance
            self.years = years
            self.data_clients[client_id]["start_balance"] = self.start_balance
            self.data_clients[client_id]["years"] = self.years
            logger.info(f"Открыт депозит клиента {self.data_clients[client_id]['name']} "
                        f"с номером {client_id}. Стартовый баланс {start_balance}. "
                        f"Срок депозита - {years} год(а)")
        else:
            logger.critical("Такого клиента не существует!")
            return "Такого клиента не существует!"

    def calc_deposit_interest_rate(self, client_id):
        deposit_itog = round(self.data_clients[client_id]["start_balance"] *
                             (1 + self.interest_rate / 12)
                             ** (12 * self.data_clients[client_id]["years"]), 2)
        logger.debug(f"У клиента {self.name} был рассчитан итоговый депозит")
        return deposit_itog

    def converter_deposit(self, client_id, out_currency):
        if client_id not in self.data_clients:
            logger.critical(f"Клиент {self.name} отсутсвует в базе")
            return "Клиент отсутсвует в базе"

        deposit_itog = self.calc_deposit_interest_rate(client_id)
        converted_value, currency = self.converter.exchange_currency("BYN",
                                                                     deposit_itog, out_currency)

        logger.info(f"Депозит клиента {self.data_clients[client_id]['name']} "
                    f"в валюте {currency}: {converted_value}")
        return converted_value, currency

    def close_deposit(self, client_id):
        if self.data_clients[client_id]["start_balance"]:
            self.data_clients[client_id]["start_balance"] = None
            self.data_clients[client_id]["years"] = None
        else:
            logger.critical(f"Клиент {self.name} сначала должен открыть депозит")
            return "Клиент сначала должен открыть депозит"
