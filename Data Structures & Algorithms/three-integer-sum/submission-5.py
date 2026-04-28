class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique = set()
        nums.sort()

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    unique.add(tuple([nums[i], nums[j], nums[k]]))
                    k -= 1
            
        
        return list(unique)
        