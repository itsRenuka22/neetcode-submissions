class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = left = right = 0
        seen = dict()

        while right < len(s):
            seen[s[right]] = 1 + seen.get(s[right], 0)
            
            rep = max(seen.values())
            window = right - left + 1

            if window - rep <= k:
                maxLen = max(maxLen, window)
                #right += 1
            else:
                seen[s[left]] -= 1
                left += 1
            
            right += 1
        
        return maxLen
        