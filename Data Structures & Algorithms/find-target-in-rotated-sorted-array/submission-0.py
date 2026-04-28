class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        index = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                index = mid
                break

            #Decide in which array you are
            #Left array
            elif (nums[mid] >= nums[left]):
                # target < mid
                if target < nums[mid]:
                    if target < nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
                # target > mid 
                else:
                    left = mid + 1
            #Right array
            else:
                # target > mid
                if target > nums[mid]:
                    if target > nums[right]:
                        right = mid - 1
                    else:
                        left = mid + 1
                # target < mid
                else:
                    right = mid - 1

        return index