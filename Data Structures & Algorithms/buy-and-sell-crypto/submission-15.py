class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_p = 0

        for right in range(1, len(prices)):
            
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_p = max(profit, max_p)
            else:
                left = right
        
        return max_p
        