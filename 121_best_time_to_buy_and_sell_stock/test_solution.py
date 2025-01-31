from solution import SingleTransactionProfitStrategy, ProfitContext

import unittest


class SolutionTestCase(unittest.TestCase):
    def test_execute_single_transaction_profit_strategy(self) -> None:
        """
        Test the `calculate_max_profit` method of `ProfitContext` using the `SingleTransactionProfitStrategy` on
        a variety of price lists.

        Dependency Inversion Principle: The use of ProfitContext to handle different strategies shows good adherence to
        this principle.
        """
        test_cases = [
            ([10, 10, 10, 10], 0),
            ([], 0),
            ([5], 0),
            ([2, 1, 1], 0),
            ([7, 1, 5, 3, 6, 4], 5),
            ([7, 6, 4, 3, 1], 0),
        ]
        context = ProfitContext(SingleTransactionProfitStrategy())

        for prices, expected_profit in test_cases:
            profit: int = context.calculate_max_profit(prices)

            self.assertEqual(profit, expected_profit)
