class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = length = max_length = 0
        seen = set()

        for right in range(len(s)):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(s[right])
            length = right - left + 1
            max_length = max(length, max_length)

        print(seen)
        return max_length


        