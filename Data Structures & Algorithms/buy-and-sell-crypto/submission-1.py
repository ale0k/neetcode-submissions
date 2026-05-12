class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = 100
        sell_price = 0
        max_profit = 0
        for price in prices:
            if price < buy_price:
                buy_price = price
                sell_price = price
            else:
                sell_price = max(sell_price, price)
            max_profit = max(max_profit, sell_price - buy_price)
        
        return max_profit
