class Bank:
    interest_rate = 0.1

    def __init__(self):
        self.bank_client_id = 1
        self.data_name = {}
        self.data_balance = {}
        self.data_years = {}

    def register_client(self, name):
        client_id = str(self.bank_client_id).zfill(7)
        self.name = name
        self.data_name[client_id] = name
        self.bank_client_id += 1
        print(f"Приветствуем нового клиента банка {name} "
              f"с индивидуальным номером {client_id}")

    def open_deposit_account(self, client_id, start_balance, years):
        self.client_id = client_id
        self.start_balance = start_balance
        self.years = years
        self.data_balance[client_id] = self.start_balance
        self.data_years[client_id] = self.years
        print(f"Открыт депозит клиента {self.data_name[client_id]} с номером "
              f"{client_id}. Стартовый баланс {start_balance}."
              f" Срок депозита - {years} год(а)")

    def calc_deposit_interest_rate(self, client_id):
        deposit_itog = round(self.data_balance[client_id] *
                             (1 + self.interest_rate / 12)
                             ** (12 * self.data_years[client_id]), 2)
        print(f"У клиента {self.data_name[client_id]} с номером {client_id}"
              f" итоговый баланс по окончанию срока действия депозита "
              f"через {self.data_years[client_id]} год(а) будет равен "
              f"{deposit_itog}")
        return deposit_itog

    def close_deposit(self, client_id):
        print(f"Клиент {self.data_name[client_id]} решает "
              f"закрыть свой депозит")
        del self.data_balance[client_id]
        del self.data_years[client_id]


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
