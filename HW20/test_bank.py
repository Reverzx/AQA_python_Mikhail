import unittest
from HW12.Bank_deposit import Bank
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()
        self.bank.register_client(name="Test")
        self.client_id = '0000001'

    def test_register_client(self):
        self.assertEqual(self.bank.data_clients[self.client_id]["name"], "Test")
        self.assertIsNone(self.bank.data_clients[self.client_id]["start_balance"])
        self.assertIsNone(self.bank.data_clients[self.client_id]["years"])

    def test_open_deposit_account_success(self):
        self.bank.open_deposit_account(self.client_id, start_balance=1000, years=1)
        self.assertEqual(self.bank.data_clients[self.client_id]["start_balance"], 1000)
        self.assertEqual(self.bank.data_clients[self.client_id]["years"], 1)

    def test_open_deposit_account_fail(self):
        result = self.bank.open_deposit_account('9000000', start_balance=1000, years=1)
        self.assertEqual(result, 'Такого клиента не существует!')

    def test_calc_deposit_interest_rate(self):
        self.bank.open_deposit_account(self.client_id, start_balance=1000, years=1)
        result = self.bank.calc_deposit_interest_rate(self.client_id)
        # Я тут поставил допустимую погрешность в 0,1 на всякий случай,
        # числа с плавающей точкой могут ведь погрешность давать
        self.assertAlmostEqual(result, 1104.71, delta=0.1)

        self.bank.open_deposit_account(self.client_id, start_balance=2000, years=2)
        result_2 = self.bank.calc_deposit_interest_rate(self.client_id)
        self.assertAlmostEqual(result_2, 2440.78, delta=0.1)

    def test_converter_deposit(self):
        self.bank.open_deposit_account(self.client_id, start_balance=1000, years=1)
        amount, currency = self.bank.converter_deposit('0000001', 'USD')
        self.assertAlmostEqual(amount, 340.96, delta=0.1)
        self.assertEqual(currency, 'USD')

    def test_close_deposit_success(self):
        self.bank.open_deposit_account(self.client_id, start_balance=1000, years=1)
        self.bank.close_deposit(self.client_id)
        self.assertIsNone(self.bank.data_clients[self.client_id]["start_balance"])
        self.assertIsNone(self.bank.data_clients[self.client_id]["years"])

    def test_close_deposit_fail(self):
        self.assertEqual(self.bank.close_deposit(self.client_id), "Клиент сначала должен открыть депозит")


if __name__ == '__main__':
    unittest.main()
