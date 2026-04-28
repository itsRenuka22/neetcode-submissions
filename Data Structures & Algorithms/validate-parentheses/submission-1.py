class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            if char in pairs: #check if closing bracket
                if stack and stack[-1] == pairs[char]: #check if stack not empty to pop and characters match
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return (len(stack) == 0)
        