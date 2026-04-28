class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        """
        rob1 = rob2 = [0] * (n-1)

        rob1[0], rob1[1] = nums[0], max(nums[0], nums[1])
        rob2[0], rob2[1] = nums[1], max(nums[1], nums[2])

        for i in range(2, n):
        
        """

        def helper(l, r):
            first = second = 0

            for i in range(l, r+1):
                first, second = second, max(first + nums[i], second)
            
            return second

        case1 = helper(0, n-2)
        case2 = helper(1, n-1)

        return max(case1, case2)
        