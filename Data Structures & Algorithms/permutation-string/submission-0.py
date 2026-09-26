class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = dict() 
        s2_freq = dict()
        l = 0

        for char in s1:
            s1_freq[char] = s1_freq.get(char, 0) + 1
        
        for r in range(len(s1)-1):
            s2_freq[s2[r]] = s2_freq.get(s2[r], 0) + 1
        
        for r in range(len(s1)-1, len(s2)):
            s2_freq[s2[r]] = s2_freq.get(s2[r], 0) + 1

            if s1_freq == s2_freq:
                return True
            else:
                if s2_freq[s2[l]] == 1:
                    s2_freq.pop(s2[l])
                else:
                    s2_freq[s2[l]] -= 1
                l += 1
        
        return False

        