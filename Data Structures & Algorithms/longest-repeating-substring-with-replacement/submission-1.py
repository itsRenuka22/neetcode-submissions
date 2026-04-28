class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = max_len = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            if ((right - left + 1) - (max(count.values())) > k):
                count[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len
        