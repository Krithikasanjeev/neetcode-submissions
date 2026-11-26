class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cost = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_cost:
                min_cost = price

            profit = price - min_cost

            if profit > max_profit:
                max_profit = profit

        return max_profit