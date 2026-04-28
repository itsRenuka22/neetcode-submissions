class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = dict()

        #Add char count in s_dict 
        for char in s:
            s_dict[char] = 1 + s_dict.get(char, 0)
        
        print(s_dict)
        #Reduce char count in s_dict as per char in t
        for char in t:
            if char in s_dict:
                s_dict[char] -= 1
                if s_dict[char] == 0:
                    s_dict.pop(char)
            else:
                return False
        
        print(s_dict)

        return True if len(s_dict) == 0 else False


        