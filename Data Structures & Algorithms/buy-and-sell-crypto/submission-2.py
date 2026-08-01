class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                buy_price = prices[r]
                l = r

            profit = prices[r] - prices[l]
            if profit > max_profit:
                max_profit = profit
                
        return max_profit