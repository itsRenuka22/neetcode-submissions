class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temp = set()
        nums.sort()

        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while(j < k):
                if(nums[i] + nums[j] + nums[k] == 0):
                    temp.add(tuple(sorted((nums[i], nums[j], nums[k]))))
                    k -= 1
                elif(nums[i] + nums[j] + nums[k] > 0):
                    k -= 1
                else:
                    j += 1
        
        return list(temp)
        