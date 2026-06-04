class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = dict()
        countT = dict()

        for char in s:
            countS[char] = 1 + countS.get(char, 0)
        
        for char in t:
            countT[char] = 1 + countT.get(char, 0)


        if countS.items() == countT.items():
            return True
        
        return False