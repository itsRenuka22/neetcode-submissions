class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        while k > 0:
            max_num = max(count, key=count.get)
            res.append(max_num)
            count.pop(max_num)
            k -= 1
        
        return res
        