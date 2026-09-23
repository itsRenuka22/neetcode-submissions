class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy = 0
        sell = 1

        while (sell < len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
            
            sell += 1
        
        return maxP
        