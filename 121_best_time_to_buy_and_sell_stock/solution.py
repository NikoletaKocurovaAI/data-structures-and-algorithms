from abc import ABC, abstractmethod


class ProfitStrategy(ABC):
    """
    Best Time to Buy and Sell Stock.

    Adhering to the Open/Closed Principle (OCP) by allowing for future extensions to support different trading
    strategies (e.g., multiple transactions) without modifying the core logic. The strategy pattern is used to
    encapsulate different profit calculation algorithms.
    """
    @abstractmethod
    def execute(self, data: list[int]) -> int:
        pass


class ProfitContext:
    def __init__(self, strategy: ProfitStrategy):
        self._strategy = strategy

    def calculate_max_profit(self, prices: list[int]) -> int:
        return self._strategy.execute(prices)


class SingleTransactionProfitStrategy(ProfitStrategy):
    def execute(self, prices: list[int]) -> int:
        """
        Concrete strategy.

        Given a list of prices, returns the maximum profit by choosing a single day to buy one stock and choosing
        a different day in the future to sell that stock.

        Time complexity: O(n), where n is the length of the prices list.
        Space complexity: O(1), since only a few integer variables are used.

        :param prices: list[int]: List of prices where prices[i] is the price of a stock on the i-th day.
        :return: int: Maximum profit achievable by buying and selling once.

        :example:
        Do not use example:
        Below approach takes O(n^2) when initializing buying_at_idx and in the loop it allocates new subarray in memory.

        buying_at_idx: int = prices.index(min(prices))

        for idx, price in enumerate(prices[buying_at_idx + 1:]):
            // logic

        for idx in range(buying_at_idx + 1, len(prices)):
            // logic
        """
        if not prices:
            return 0

        min_price_so_far: int | float = float('inf')
        max_profit: int = 0

        for current_day_price in prices:
            min_price_so_far = min(min_price_so_far, current_day_price)

            current_day_profit: int = current_day_price - min_price_so_far
            max_profit: int = max(max_profit, current_day_profit)

        return max_profit
