class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 0

        while (l <= r):
            mid = math.floor((l + r) / 2)
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)
            
            if hours > h:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1
        
        return ans
        