class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = max_len = 0
        seen = set()

        while(right < len(s)):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(s[right])
            length = right - left + 1
            max_len = max(max_len, length)
            right += 1
        
        return max_len
        