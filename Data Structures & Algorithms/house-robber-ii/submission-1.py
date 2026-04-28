class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(l,r):
            first = second = 0
            for i in range(l, r+1):
                curr = max(first + nums[i], second)
                first, second = second, curr

            return second
        
        case1 = helper(0, n-2)
        case2 = helper(1, n-1)

        return max(case1, case2)
        