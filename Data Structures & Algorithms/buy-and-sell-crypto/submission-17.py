class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 1
        maxP = 0

        while s < len(prices):
            profit = prices[s] - prices[b]

            if profit < 0:
                b = s
            else:
                maxP = max(profit, maxP)
            
            s += 1
        
        return maxP
        