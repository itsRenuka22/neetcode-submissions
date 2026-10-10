class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while (l <= r):
            #sorted array
            if (nums[l] < nums[r]):
                return min(res, nums[l])

            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]: #left sorted array --> search right
                l = mid + 1
            else: #right sorted array --> search left
                r = mid - 1
        
        return res

        