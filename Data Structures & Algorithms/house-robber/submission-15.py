class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        robbed = [0] * (n)
        robbed[0], robbed[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            robbed[i] = max(robbed[i-1], robbed[i-2] + nums[i])
        
        return robbed[-1]
        