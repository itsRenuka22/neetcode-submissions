class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = dict()
        s_freq = dict()
        minL = len(s) + 1
        l = 0
        have = 0
        res = ""

        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1
        
        need = int(len(t_freq.keys()))

        for r in range(len(s)):
            s_freq[s[r]] = s_freq.get(s[r], 0) + 1

            if s[r] in t_freq and s_freq[s[r]] == t_freq[s[r]]:
                have += 1
            
            while have == need:
                currLen = r - l + 1
                if currLen < minL:
                    res = s[l:r+1]
                    minL = currLen
                s_freq[s[l]] -= 1

                if s[l] in t_freq and s_freq[s[l]] < t_freq[s[l]]:
                    have -= 1
                
                l += 1
        
        return res
        