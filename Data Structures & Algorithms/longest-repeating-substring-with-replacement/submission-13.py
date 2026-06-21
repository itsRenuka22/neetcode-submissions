class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        l = r = 0
        maxLen = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            window = r - l + 1
            repl = window - max(count.values())

            if repl <= k:
                maxLen = max(maxLen, window)
            else:
                count[s[l]] -= 1
                l += 1
        
        return maxLen
        