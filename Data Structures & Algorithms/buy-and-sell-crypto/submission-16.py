class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        b = 0
        s = 1

        while s < len(prices):
            if prices[b] < prices[s]:
                profit = prices[s] - prices[b]
                maxP = max(maxP, profit)
            
            else:
                b = s
            
            s += 1
        
        return maxP
        
        