class Solution:
    def encode(self, strs: List[str]) -> str:
        new_word = ""
        for word in strs:
            length = len(word)
            new_word += str(length)+"&"+word
        print(new_word)
        return new_word

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while (s[j] != "&"):
                j += 1
            length = int(s[i:j])
            word = s[j+1: j+1+length]
            res.append(word)
            i = j+1+length
        return res
        

