class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        left = 0
        right = 0
        maxL = 0

        while (right < len(s)):
            if s[right] in res:
                while s[right] in res:
                    res.remove(s[left])
                    left += 1
            res.add(s[right])
            length = right - left + 1
            maxL = max(maxL, length)
            right += 1
        
        return maxL
