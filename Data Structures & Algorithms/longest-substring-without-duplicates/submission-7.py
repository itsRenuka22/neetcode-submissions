class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = longest = 0
        seen = dict()
        for right in range(len(s)):
            while s[right] in seen:
                seen.pop(s[left])
                left += 1
            seen[s[right]] = right
            length = right - left + 1
            longest = max(longest, length)
        
        return longest
        