class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == "0":
            return 0
        
        #dp = [0] * (n+1)
        prev2 = 1
        prev1 = 1

        for i in range(2, n+1):
            curr = 0
            if s[i-1:i] != '0':
                curr += prev1
            if 10 <= int(s[i-2:i]) <= 26:
                curr += prev2

            prev2, prev1 = prev1, curr
            #print(curr)

        return prev1
        