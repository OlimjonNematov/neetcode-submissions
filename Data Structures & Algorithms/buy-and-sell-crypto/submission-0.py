class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        # loop through each day
        for day, daily_price in enumerate(prices):
            future_prices: prices

            for day in range(day, len(prices)):
                print(daily_price, prices[day])
                curr_profit = prices[day] - daily_price
                profit = max(curr_profit, profit)
                print(profit)



        return profit