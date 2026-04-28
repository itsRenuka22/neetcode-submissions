class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - buy_price
            
            if profit > max_profit:
                max_profit = profit  
            
            else: 
                if buy_price > prices[i]:
                    buy_price = prices[i]

        return max_profit        