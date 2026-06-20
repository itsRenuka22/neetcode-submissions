class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temp = set()
        nums.sort()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while (j < k):
                
                threeSum = nums[i] + nums[j] + nums[k]
                
                if threeSum < 0:
                    j += 1
                elif threeSum > 0:
                    k -= 1
                else:
                    temp.add(tuple((nums[i], nums[j], nums[k])))
                    j += 1
                    k -= 1


        return [list(t) for t in temp] 
        