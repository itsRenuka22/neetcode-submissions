class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = longest = 0
        seen = dict()

        for right in range(len(s)):
            seen[s[right]] = 1 + seen.get(s[right], 0)

            window = right - left + 1
            replace = window - max(seen.values())

            if replace <= k:
                longest = max(longest, window)
            else:
                seen[s[left]] -= 1
                left += 1

        return longest        