class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = len(word)
            encoded += str(length) + "#" + word
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            #print(s[j+1:j+length])
            word = s[j+1:j+length+1]
            res.append(word)
            i = j+length+1
        
        return res
    

        

            
            
        
