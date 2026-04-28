class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        
        for word in strs:
            charFreq = [0] * 26
            for char in word:
                charFreq[ord(char) - ord('a')] += 1

            group[tuple(charFreq)].append(word)
        
        return list(group.values())
        