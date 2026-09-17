class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        res = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                pre[i] = 1
            else:
                pre[i] = pre[i-1] * nums[i-1]
        
        for i in range(len(nums)-1, -1,-1):
            if i == len(nums)-1:
                post[i] = 1
            else:
                post[i] = post[i+1] * nums[i+1]

        for i in range(len(nums)):
            res[i] = pre[i] * post[i]
        
        return res