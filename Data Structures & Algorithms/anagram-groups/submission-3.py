class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = dict()

        for word in strs:
            charMap = [0]*26
            for char in word:
                charMap[ord(char) - ord("a")] += 1
           
            key = tuple(charMap)

            if key not in group:
                group[key] = []
            group[key].append(word)
        
        return list((group.values()))
        