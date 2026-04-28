class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'}':'{', ']':'[', ')':'('}
        seen = []

        if s[0] in pair.keys():
            return False 

        for char in s:
            if char not in pair:
                seen.append(char)
            else:
                if len(seen) != 0 and seen.pop(-1) == pair[char]:
                    continue
                else:
                    return False
        
        return True if len(seen) == 0 else False
        