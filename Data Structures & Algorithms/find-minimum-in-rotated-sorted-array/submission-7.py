class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[0]

        while (left <= right):
            if nums[left] < nums[right]:
                return min(res,nums[left])
                break
            mid = (left + right) // 2
            res = min(res, nums[mid])

            #left sorted
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid -1
            
        return res
        