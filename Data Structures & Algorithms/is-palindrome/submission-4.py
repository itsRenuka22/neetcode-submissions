class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for char in s:
            if char.isalnum():
                new += char.lower()
    
        i = 0
        j = len(new) - 1

        while i <= j:
            if new[i] != new[j]:
                return False
            i += 1
            j -= 1
        
        return True
        