class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = largest = nums[0]

        for i in range(1, len(nums)):
            current = max(current + nums[i], nums[i])
            largest = max(current, largest)

        return largest
        