class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small, large = 0, len(numbers) - 1

        while small < large:
            if (numbers[small] + numbers[large]) == target:
                return [small+1, large+1]
            elif (numbers[small] + numbers[large]) < target:
                small += 1
            else:
                large -= 1
        
        return [0,0]


        