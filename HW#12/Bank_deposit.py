class Bank:
    interest_rate = 0.1

    def __init__(self):
        self.start_balance = None
        self.name = None
        self.years = None
        self.client_id = '0000001'
        self.data_clients = {}

    def register_client(self, name):
        self.name = name
        self.data_clients[self.client_id] = {
            "name": name,
            "start_balance": None,
            "years": None
        }
        print(f"Приветствуем нового клиента банка {name} "
              f"с индивидуальным номером {self.client_id}")
        self.client_id = f"{(int(self.client_id) + 1):07d}"

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id in self.data_clients:
            self.client_id = client_id
            self.start_balance = start_balance
            self.years = years
            self.data_clients[client_id]["start_balance"] = self.start_balance
            self.data_clients[client_id]["years"] = self.years
            print(f"Открыт депозит клиента {self.data_clients[client_id]['name']} с номером "
                  f"{client_id}. Стартовый баланс {start_balance}."
                  f" Срок депозита - {years} год(а)")
        else:
            print("Такого клиента не существует!")

    def calc_deposit_interest_rate(self, client_id):
        deposit_itog = round(self.data_clients[client_id]["start_balance"] *
                             (1 + self.interest_rate / 12)
                             ** (12 * self.data_clients[client_id]["years"]), 2)
        print(f"У клиента {self.data_clients[client_id]["name"]} с номером {client_id}"
              f" итоговый баланс по окончанию срока действия депозита "
              f"через {self.data_clients[client_id]["years"]} год(а) будет равен "
              f"{deposit_itog}")
        return deposit_itog

    def close_deposit(self, client_id):
        if self.data_clients[client_id]["start_balance"]:
            print(f"Клиент {self.data_clients[client_id]["name"]} решает "
                  f"закрыть свой депозит")
            self.data_clients[client_id]["start_balance"] = None
            self.data_clients[client_id]["years"] = None
        else:
            print("Клиент сначала должен открыть депозит")


bank = Bank()
bank.register_client(name="Pavel")
bank.register_client(name="Misha")
bank.open_deposit_account('0000001', start_balance=1000, years=1)
bank.open_deposit_account('0000002', start_balance=2000, years=2)

bank.calc_deposit_interest_rate('0000001')
bank.calc_deposit_interest_rate('0000002')

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
