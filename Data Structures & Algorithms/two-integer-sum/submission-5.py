class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in elements:
                return [elements[diff], i]
            elements[nums[i]] = i
            print(elements)
        print(elements)
            
        return [0,0]
        