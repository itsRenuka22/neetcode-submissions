class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = post = 1
        #res[0] = 1

        for i in range(1, len(nums)):
            pre *= nums[i-1]
            res[i] = pre
        
        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post *= nums[i]

        return res
        