class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '{':'}', '[':']'}
        seen = []

        for char in s:
            if char in pairs.keys():
                seen.append(char)
            else:
                if not seen:
                    return False
                popped = seen.pop()
                if char != pairs[popped]:
                    return False
        
        return len(seen) == 0