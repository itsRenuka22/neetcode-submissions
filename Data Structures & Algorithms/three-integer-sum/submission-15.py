class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        unique = set()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while (j < k):
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    unique.add((nums[i], nums[j], nums[k]))
                if total <= 0:
                    j += 1
                if total >= 0:
                    k -= 1
                
        return [list(t) for t in unique]
        