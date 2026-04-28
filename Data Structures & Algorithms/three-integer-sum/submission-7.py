class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        #print(sorted)

        for i in range(len(nums) - 2):
            """
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0:
                break
            """
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add(tuple([nums[i],nums[j],nums[k]]))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
            
        return list(list(t) for t in result)