class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        l = r = 0
        maxLen = 0

        for char in s:
            count[char] = 1 + count.get(char, 0)
            window = len(s[l:r]) + 1
            repl = window - max(count.values())

            if repl <= k:
                maxLen = max(maxLen, window)
            else:
                count[s[l]] -= 1
                l += 1
            r += 1
        
        return maxLen
        