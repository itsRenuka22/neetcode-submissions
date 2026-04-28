class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ele = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in ele:
                return list((ele[diff], i))
            ele[nums[i]] = i
        
        return list((0,0))
        