class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {']':'[', '}':'{', ')':'('}
        stack = []

        for i in range(len(s)):
            if s[i] not in pairs:
                stack.append(s[i])
                print(stack)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                print(stack)
                if popped != pairs[s[i]]:
                    return False
        
        print(stack)
        return (len(stack) == 0)
        