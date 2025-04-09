from HW21.source.Bank_deposit import Bank


class TestBank:

    def setup_method(self):
        self.bank = Bank()
        self.bank.register_client(name="Test")
        self.client_id = '0000001'

    def test_register_client(self):
        assert self.bank.data_clients[self.client_id]["name"] == "Test"
        assert self.bank.data_clients[self.client_id]["start_balance"] is None
        assert self.bank.data_clients[self.client_id]["years"] is None

    def test_open_deposit_account_success(self):
        self.bank.open_deposit_account(self.client_id, start_balance=1000, years=1)
        assert self.bank.data_clients[self.client_id]["start_balance"] == 1000
        assert self.bank.data_clients[self.client_id]["years"] == 1

    def test_open_deposit_account_fail(self):
        result = self.bank.open_deposit_account('9000000', start_balance=1000, years=1)
        assert result == "Такого клиента не существует!"

    def test_calc_deposit_interest_rate(self):
        self.bank.open_deposit_account(self.client_id, start_balance=1000, years=1)
        result = self.bank.calc_deposit_interest_rate(self.client_id)
        assert 1104.61 <= result <= 1104.81

    def test_converter_deposit(self):
        self.bank.open_deposit_account(self.client_id, start_balance=1000, years=1)
        amount, currency = self.bank.converter_deposit('0000001', 'USD')
        assert 340.86 <= amount <= 341.06
        assert currency == 'USD'

    def test_close_deposit_success(self):
        self.bank.open_deposit_account(self.client_id, start_balance=1000, years=1)
        self.bank.close_deposit(self.client_id)
        assert self.bank.data_clients[self.client_id]["start_balance"] is None
        assert self.bank.data_clients[self.client_id]["years"] is None

    def test_close_deposit_fail(self):
        assert self.bank.close_deposit(self.client_id) == "Клиент сначала должен открыть депозит"
