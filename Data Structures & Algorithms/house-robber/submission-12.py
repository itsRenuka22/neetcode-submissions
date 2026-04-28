class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        curr = 0

        if n == 1:
            return nums[0]
        """
        elif n == 2:
            return max(nums[0], nums[1])
        """
        
        first, second = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            curr = max(first + nums[i], second)
            first = second
            second = curr
        
        return second
        