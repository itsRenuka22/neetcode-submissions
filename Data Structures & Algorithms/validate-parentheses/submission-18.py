class Solution:
    def isValid(self, s: str) -> bool:
        #open = {"(", "[", "{"}
        pair = {"(": ")", "[": "]", "{": "}"}
        st = []
        
        for i in range(len(s)):
            if s[i] in pair:
                st.append(s[i])
            else:
                if not st:
                    return False
                top = st.pop()
                if pair[top] != s[i]:
                    return False
        
        if len(st) == 0:
            return True
        else:
            return False
        