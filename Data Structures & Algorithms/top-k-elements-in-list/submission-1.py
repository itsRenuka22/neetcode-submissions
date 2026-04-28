class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashed = {}
        final = []
        for num in nums:
            if num not in hashed:
                hashed[num] = 1
            else:
                hashed[num] += 1
        
        for i in range(k):
            maximum = max(hashed, key=hashed.get)
            final.append(maximum)
            hashed.pop(maximum)
        
        return final